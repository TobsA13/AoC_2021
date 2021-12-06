from aoc import aoc
from pprint import pprint
from collections import Counter

r1 = 0
r2 = 0

AOC = aoc(6)
LINES = AOC.read_lines()
DATA = AOC.ints(LINES[0].split(","))

#------- PART 1

DATA_R1 = DATA.copy()
for day in range(80):
    for index, data in enumerate(DATA_R1.copy()):
        if data == 0:
            DATA_R1.append(8)
            DATA_R1[index] = 6
        else:
            DATA_R1[index] -= 1
r1 = len(DATA_R1)

#------- PART 2

DATA_R2 = DATA.copy()
DATA_R2 = Counter(DATA_R2)
for day in range(256):
    DATA_R2 = {k - 1: v for k, v in DATA_R2.items()}
    if -1 in DATA_R2:
        DATA_R2[8] = DATA_R2[-1]
        DATA_R2[6] = DATA_R2.get(6, 0) + DATA_R2.pop(-1)
r2 = sum(DATA_R2.values())

print("Puzzle 1: " +str(r1))
print("Puzzle 2: " +str(r2))

#Part 1 example
#assert r1 == 5934

#Part 2 example
#assert r2 == 26984457539