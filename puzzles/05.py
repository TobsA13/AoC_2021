from copy import deepcopy

from aoc import aoc
from pprint import pprint
from collections import Counter

r1 = 0
r2 = 0

AOC = aoc(5)
LINES = AOC.read_lines()


def formatInput(lines):
    result = []
    xMax = 0
    yMax = 0
    for line in lines:
        line = line.split(" -> ")
        c1 = AOC.ints(line[0].split(","))
        c2 = AOC.ints(line[1].split(","))
        xMax = max(xMax, c1[0], c2[0])
        yMax = max(yMax, c1[1], c2[1])
        result.append([(c1[0], c1[1]), (c2[0], c2[1])])
    return xMax, yMax, result


def addLines(lines, matrix, diagonal: bool):
    for line in lines:
        if line[0][0] == line[1][0]:
            # X = X
            for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                matrix[y][line[0][0]] += 1
                pass

        elif line[0][1] == line[1][1]:
            # Y = Y
            for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                matrix[line[0][1]][x] += 1

        elif diagonal:
            # Diagonal
            if line[0][0] < line[1][0]:
                pLeft = line[0]
                pRight = line[1]
            else:
                pLeft = line[1]
                pRight = line[0]

            if pLeft[1] < pRight[1]:
                # Going down
                points = list(zip(range(pLeft[0], pRight[0] + 1), range(pLeft[1], pRight[1] + 1)))

            else:
                # Gonig up
                points = list(zip(range(pLeft[0], pRight[0] + 1), range(pLeft[1], pRight[1] - 1, -1)))

            for point in points:
                matrix[point[1]][point[0]] += 1

    return matrix


def countFields(matrix, moreoreqthan):
    sum = 0
    for row in matrix:
        for col in row:
            if col >= moreoreqthan:
                sum += 1
    return sum


XMAX, YMAX, LINES_F = formatInput(LINES)

MATRIX = [[0] * (XMAX + 1) for i in range(YMAX + 1)]

MATRIX_R1 = addLines(LINES_F, deepcopy(MATRIX), False)

r1 = countFields(MATRIX_R1, 2)

MATRIX_R2 = addLines(LINES_F, MATRIX, True)

r2 = countFields(MATRIX_R2, 2)

#pprint(MATRIX_R2)

print("R1:" + str(r1))
# Part 1 example
#assert r1 == 5
assert r1 == 8622

print("R2:" + str(r2))
# Part 2 example
#assert r2 == 12
assert r2 == 22037
