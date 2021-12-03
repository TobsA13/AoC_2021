from pathlib import Path
from typing import List



class aoc:
    def __init__(self, day: int, example: bool=False):
        self.day = day
        self.example = example
        print("Advent of Code 2021 Day {day}.\n\n".format(day=day))

    # --- Parsing -----------------------------------------------------------------

    def ints(self, s: List[str]):
        return list(map(int, s))

    def floats(self, s: List[str]):
        return list(map(float, s))

    def strips(self, s: List[str]):
        return list(map(str.strip, s))

    # --- Input -------------------------------------------------------------------

    def resolve_day(self):
        return Path("inputs/" + str(self.day) + ("e" if self.example else ""))

    def read_string(self):
        with open(self.resolve_day()) as file:
            return file.read()

    def read_lines(self, strip = True):
        with open(self.resolve_day()) as file:
            return self.strips(list(file)) if strip else list(file)

    def read_lines_int(self):
        return self.ints(self.read_lines())

    def read_lines_float(self):
        return self.floats(self.read_lines())
