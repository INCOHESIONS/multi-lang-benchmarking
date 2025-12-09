# pyright: reportMissingTypeStubs=false

import subprocess
from argparse import ArgumentParser
from pathlib import Path
from time import perf_counter_ns

import compushady
import cpuinfo
import psutil
from bconsole import ColoredFileLogger, Erase, get_logger

from program import Program
from utils import format_list, format_program_dir, format_time

parser = ArgumentParser()
parser.add_argument("--width", nargs="?", type=int, default=1000)
parser.add_argument("--height", nargs="?", type=int, default=1000)
parser.add_argument("--points", nargs="?", type=int, default=100)
parser.add_argument("--runs", nargs="?", type=int, default=10)
parser.add_argument("--save", nargs="?", type=bool, default=False)
parser.add_argument("--sort", nargs="?", type=str, default="avg")

args = parser.parse_args()

WIDTH = args.width
HEIGHT = args.height
NUMBER_OF_POINTS = args.points
SAVE_IMAGES = args.save
RUN_COUNT = args.runs
SORT_BY = args.sort

prepare_cmd = r".\prepare"
run_cmd = f".\\run.bat {WIDTH} {HEIGHT} {NUMBER_OF_POINTS} {str(SAVE_IMAGES).lower()}"

all_dirs = list(Path(__file__).resolve().parent.glob("* - *PU*"))

cpu = cpuinfo.get_cpu_info()
gpu = compushady.get_discovered_devices()[0]

header = [
    "# Worley Noise Benchmarking",
    f"> CPU: {cpu['brand_raw']} ({float(cpu['hz_advertised_friendly'].split()[0]):.2f} GHz) |",
    f"> GPU: {gpu.name} |",
    f"> approx. RAM: {psutil.virtual_memory().total // (1024**2):.0f} MB |",
    f"> approx. VRAM: {gpu.dedicated_video_memory // (1024**2):.0f} MB |",
    f"> Width: {WIDTH}; Height: {HEIGHT}; Number of points: {NUMBER_OF_POINTS} |",
    f"> {len(all_dirs)} programs, {RUN_COUNT + 1} runs each (1st run is discarded and not included)",
]

if len(all_dirs) == 0:
    raise RuntimeError("No directories were found.")

for dir in all_dirs:
    if not any(file.name == "run.bat" for file in dir.iterdir()):
        raise RuntimeError(f"{format_program_dir(dir)}: directory lacks run.bat")


formatted_list = format_list(", ".join(map(format_program_dir, all_dirs)))[:-1]

logger = get_logger(
    "Worley Noise Benchmarking", ColoredFileLogger.from_path("./logs.log")
)

logger.info(f"Beginning benchmarking {len(all_dirs)} programs: {formatted_list}.\n")

programs: list[Program] = []

start = perf_counter_ns()

for dir in all_dirs:
    name = format_program_dir(dir)

    if any(file.name == "prepare.bat" for file in dir.iterdir()):
        logger.info(f"{name}: preparing")
        subprocess.run(
            prepare_cmd,
            cwd=dir,
            text=True,
            check=True,
            shell=True,
            stdin=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
    else:
        logger.info(f"{name}: skipping prep")

    logger.info(f"{name}: beginning runs")

    timings: list[float] = []

    for run in range(RUN_COUNT + 1):
        discard = run == 0  # first run is discarded

        logger.debug(f"{name}: executing run #{run}...")

        try:
            result = subprocess.run(
                run_cmd, cwd=dir, capture_output=True, text=True, check=True, shell=True
            )
        except:
            logger.error(f"{name}: error at run #{run}")
            raise

        out = result.stdout
        time = float(
            out.strip() if "\n" not in out else out.strip().split("\n")[-1].strip()
        )

        print("".join(*Erase.lines()), end="")

        logger.debug(
            f"{name}: run #{run} took {format_time(time)}."
            + (" (discarded)" if discard else "")
        )

        if discard:
            continue

        timings.append(time)

    programs.append(program := Program.from_timings(dir, timings))

    is_last = dir == all_dirs[-1]

    extra = (
        f"(took {format_time(program.total)})"
        if is_last
        else f"(took {format_time(program.total)}, {format_time(perf_counter_ns() - start)} so far)"
    )

    logger.info(f"{name}: finished {extra}.\n")

logger.info(
    f"Benchmarking done! (total runtime: {format_time(perf_counter_ns() - start)})."
)

programs.sort(key=lambda program: getattr(program, SORT_BY))

best_avg = min(programs, key=lambda p: p.avg)
worst_avg = max(programs, key=lambda p: p.avg)

summary = [
    "## Summary",
    f"> sorted by {SORT_BY}",
    "",
    "|  Program  |  Average  |  Min  |  Max  |   Total   |  Diff  |",
    "|-----------|:---------:|:-----:|:-----:|:---------:|:------:|",
    *(
        f"| {program.formatted_name} | {program.formatted_info} | {program.avg / best_avg.avg:.2f}x"
        for program in programs
    ),
]

stats = [
    "## Stats",
    "",
    f"- total time taken: `{format_time(perf_counter_ns() - start)}`.",
    f"- total time taken (just runs): `{format_time(sum(program.total for program in programs))}`.",
    f"- best avg: {best_avg.formatted_name} `({format_time(best_avg.avg)})`.",
    f"- worst avg: {worst_avg.formatted_name} `({format_time(worst_avg.avg)})`.",
]

separator = ["", "---", ""]


with open("RESULTS.md", mode="w+t", encoding="utf-8") as file:
    file.writelines(
        (line + "\n" for line in [*header, *separator, *summary, *separator, *stats])
    )

logger.info("Results were saved to RESULTS.md.")
