from pathlib import Path

class aoc:
    def __init__(self, day: int, suffix: str = ""):
        self.day = day
        self.suffix = suffix
        print("Advent of Code 2021 Day {day}.\n\n".format(day=day))

    # --- Parsing -----------------------------------------------------------------

    def ints(self, s: list[str]):
        return list(map(int, s))

    def floats(self, s: list[str]):
        return list(map(float, s))

    # --- Input -------------------------------------------------------------------

    def resolve_day(self):
        return Path("inputs/" + str(self.day) + self.suffix)

    def read_string(self):
        with open(self.resolve_day()) as file:
            return file.read()

    def read_lines(self):
        with open(self.resolve_day()) as file:
            return list(file)

    def read_lines_int(self):
        return self.ints(self.read_lines())

    def read_lines_float(self):
        return self.floats(self.read_lines())
