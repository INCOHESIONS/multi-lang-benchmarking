from pathlib import Path


def format_program_dir(path: Path, /, *, stylize: bool = False) -> str:
    language, rest = path.name.split(" - ")

    if "," in rest:
        device, library = rest.split(", ")
    else:
        device = rest
        library = False

    formatted = f"{language}{f' *with {library}*' if library else ''} **({device})**"
    return formatted if stylize else formatted.replace("*", "")


def format_list(text: str, /, *, period: bool = True) -> str:
    return replace_last(text, ", ", " and ") + ("." if period else "")


def format_time(ns: float, /, *, only_seconds: bool = False) -> str:
    if only_seconds:
        return f"{ns / 1e9:.3f}"

    if ns < 1_000:
        return f"{ns:.0f}ns"

    us = ns / 1_000
    if us < 1_000:
        return f"{us:.3f}µs"

    ms = us / 1_000
    if ms < 1_000:
        return f"{ms:.3f}ms"

    sec = ms / 1_000
    if sec < 60:
        return f"{sec:.3f}s"

    minutes, seconds = divmod(sec, 60)
    return f"{str(int(minutes)).rjust(2, '0')}:{str(int(seconds)).rjust(2, '0')}min"


def replace_last(text: str, old: str, new: str, /) -> str:
    return new.join(text.rsplit(old, 1))
