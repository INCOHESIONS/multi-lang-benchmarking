# pyright: reportMissingTypeStubs=false

import subprocess
from pathlib import Path
from time import perf_counter

import compushady
import cpuinfo
import psutil
from bconsole import ColoredFileLogger, Erase, get_logger


def format_dir_name(dir: Path, /) -> str:
    language, device = dir.name.split(" - ")
    return f"{language} ({device})"


def replace_last(text: str, old: str, new: str, /) -> str:
    return new.join(text.rsplit(old, 1))


def format_list(text: str, /) -> str:
    return replace_last(text, ", ", " and ") + "."


def format_time(seconds: float, /) -> str:
    if seconds > 60:
        minutes, seconds = divmod(seconds, 60)
        return f"{str(int(minutes)).rjust(2, '0')}:{int(seconds)}min"
    return f"{seconds:.3f}s"


def format_timings(timings: list[float], /) -> str:
    total = sum(timings)
    avg = total / len(timings)
    minimum = min(timings)
    maximum = max(timings)
    return format_list(
        ", ".join(map(lambda t: f"`{format_time(t)}`", (total, avg, minimum, maximum)))
    )


WIDTH = 1000
HEIGHT = 1000
NUMBER_OF_POINTS = 100
SAVE_IMAGES = False
RUN_COUNT = 10

logger = get_logger(
    "Worley Noise Benchmarking", ColoredFileLogger.from_path("./logs.log")
)

all_dirs = list(Path(__file__).resolve().parent.glob("* - *PU*"))

if len(all_dirs) == 0:
    raise RuntimeError("No directories were found.")

perf: dict[Path, list[float]] = {dir: [] for dir in all_dirs}

for dir in all_dirs:
    if not any(file.name == "run.bat" for file in dir.iterdir()):
        name = format_dir_name(dir)
        raise RuntimeError(f"{name}: directory lacks run.bat")

logger.info(
    f"Beginning runs for {len(all_dirs)} programs ({format_list(', '.join(map(format_dir_name, all_dirs)))[:-1]}).\n"
)

start = perf_counter()

for dir in all_dirs:
    name = format_dir_name(dir)

    if any(file.name == "prepare.bat" for file in dir.iterdir()):
        logger.info(f"{name}: preparing")
        subprocess.run(
            "prepare.bat",
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

    cmd = f".\\run.bat {WIDTH} {HEIGHT} {NUMBER_OF_POINTS} {str(SAVE_IMAGES).lower()}"

    for run in range(RUN_COUNT + 1):
        discard = run == 0  # first run is discarded

        logger.debug(f"{name}: executing run #{run}...")

        try:
            result = subprocess.run(
                cmd, cwd=dir, capture_output=True, text=True, check=True, shell=True
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

        perf[dir].append(time)

    logger.info(
        f"{name}: finished (took {format_time(sum(perf[dir]))}, {format_time(perf_counter() - start)} so far).\n"
    )

cpu = cpuinfo.get_cpu_info()
gpu = compushady.get_discovered_devices()[0]

lines = [
    "# Worley Noise Benchmarking |\n",
    f"> CPU: {cpu['brand_raw']} ({cpu['hz_advertised_friendly']} GHz) |\n",
    f"> GPU: {gpu.name} |\n",
    f"> RAM: {round(psutil.virtual_memory().total / (1024**2), 2)} MB |\n",
    f"> VRAM: {gpu.dedicated_video_memory // (1024**2)} MB |\n",
    f"> Width: {WIDTH}; Height: {HEIGHT}; Number of points: {NUMBER_OF_POINTS} |\n",
    f"> {len(all_dirs)} programs, {RUN_COUNT + 1} runs each (1st run is discarded and not included)\n\n",
    "## Summary\n",
    "> run - total, avg, min and max\n\n",
]

lines.extend(
    f"- {format_dir_name(dir)} - {format_timings(timings)}\n"
    for dir, timings in perf.items()
)

dashes = "\n" + "-" * max(len(line) for line in lines) + "\n\n"

lines.insert(7, dashes[1:])
lines.append(dashes)
lines.append("## All runs\n")
lines.append("> run - timings\n\n")

lines.extend(
    f"- {format_dir_name(dir)} - {format_list(', '.join(map(lambda t: f'`{format_time(t)}`', timings)))}\n"
    for dir, timings in perf.items()
)

lines.append(dashes)

lines.append("## Stats\n\n")

best_run = min(perf.items(), key=lambda i: sum(i[1]) / len(i))
worst_run = max(perf.items(), key=lambda i: sum(i[1]) / len(i))

lines.append(f"- best avg: `{format_dir_name(best_run[0])}`.\n")
lines.append(f"- worst avg: `{format_dir_name(worst_run[0])}`.\n")
lines.append(
    f"- total time taken (just runs): `{format_time(sum(sum(timings) for timings in perf.values()))}`.\n"
)
lines.append(
    f"- total time taken (including prep): `{format_time(perf_counter() - start)}`.\n"
)

lines.append(dashes[:-2])

with open("RESULTS.md", mode="w+t", encoding="utf-8") as file:
    file.writelines(lines)

logger.warning("Done!")
