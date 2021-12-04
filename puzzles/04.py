from aoc import aoc
from pprint import pprint
from collections import Counter

aoc = aoc(4)
lines = aoc.read_lines()
r1 = 0
r2 = 0

numbers = aoc.ints(lines.pop(0).split(","))

bingoFields = []
bingoField = []
for line in lines:
    if line.strip() == "":
        if len(bingoField) > 0:
            bingoFields.append(bingoField)
        bingoField = []
        continue
    bingoField.append(list(zip(aoc.ints(line.replace("  ", " ").split(" ")), [False] * 5)))

bingoFields.append(bingoField)


def checkIfWon(bingoField):
    for row in bingoField:
        temp = []
        for el in row:
            temp.append(el[1])
        if temp[0] and all(temp):
            return True
    for rowI in range(len(bingoField[0])):
        temp = []
        for colI in range(len(bingoField)):
            temp.append(bingoField[colI][rowI][1])
        if temp[0] and all(temp):
            return True


def fillAndCheck(numbers):
    won_fields = []
    for number in numbers:
        for bingoFieldI, bingoField in enumerate(bingoFields):
            if not checkIfWon(bingoField):
                for rowI, row in enumerate(bingoField):
                    for elementI, element in enumerate(row):
                        if element[0] == number:
                            bingoFields[bingoFieldI][rowI][elementI] = (element[0], True)
                            if checkIfWon(bingoField):
                                won_fields.append([number, bingoField])
    return won_fields

def sumNonHit(bingoField):
    SUM = 0
    for row in bingoField:
        for el in row:
            if not el[1]:
                SUM += el[0]
    return SUM

fields = fillAndCheck(numbers)
r1 = fields[0][0] * sumNonHit(fields[0][1])

pprint(fields[0])
print("r1: " + str(r1))

r2 = fields[-1][0] * sumNonHit(fields[-1][1])
pprint(fields[-1])
print("r2: " + str(r2))
# Part 1 example
#assert r1 == 4512

# Part 2 example
# assert r2 == 0
