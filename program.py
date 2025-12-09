from dataclasses import dataclass
from pathlib import Path
from typing import Self, final

from utils import format_list, format_program_dir, format_time

__all__ = ["Program"]


@final
@dataclass
class Program:
    path: Path
    timings: list[float]
    total: float
    avg: float
    min: float
    max: float

    @classmethod
    def from_timings(cls, path: Path, timings: list[float], /) -> Self:
        return cls(
            path,
            timings,
            total := sum(timings),
            total / len(timings),
            min(timings),
            max(timings),
        )

    @property
    def formatted_name(self) -> str:
        return format_program_dir(self.path, stylize=True)

    @property
    def formatted_timings(self) -> str:
        return format_list(
            ", ".join(map(lambda t: f"`{format_time(t)}`", self.timings))
        )

    @property
    def formatted_info(self) -> str:
        return format_list(
            " | ".join(
                map(
                    lambda t: f"`{format_time(t)}`",
                    (self.avg, self.min, self.max, self.total),
                )
            ),
            period=False,
        )
