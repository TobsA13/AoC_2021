from aoc import aoc
from pprint import pprint
from collections import Counter
from statistics import median, mean

r1 = 0
r2 = 0

AOC = aoc(7)
LINES = AOC.read_lines()
DATA = AOC.ints(LINES[0].split(","))

# -- part 1
r1 = int(sum([abs(x-median(DATA)) for x in DATA]))


# -- part 2
def calc_fuel(crab, i):
    #Gauß der Alpha Chad
    dist = abs(crab-i)
    return dist * (dist + 1) / 2

r2 = int(min([sum(map(lambda crab: calc_fuel(crab, i), DATA)) for i in range(min(DATA), max(DATA))]))


print("Puzzle 1: " +str(r1))
print("Puzzle 2: " +str(r2))
#Part 1 example
assert r1 == 37

#Part 2 example
assert r2 == 168