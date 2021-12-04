from aoc import aoc

aoc = aoc(2)

lines = aoc.read_lines()

h = 0
d = 0

for l in lines:
    l = l.split(" ")
    if l[0] == "forward":
        h += int(l[1])
    elif l[0] == "up":
        d -= int(l[1])
    elif l[0] == "down":
        d += int(l[1])

print("H: " + str(h))
print("D: " + str(d))
print("Result: " + str(h*d))

h = 0
d = 0
a = 0

for l in lines:
    l = l.split(" ")
    v = int(l[1])
    if l[0] == "forward":
        h += v
        d += a * v
    elif l[0] == "up":
        a -= v
    elif l[0] == "down":
        a += v

print("H: " + str(h))
print("D: " + str(d))
print("Result: " + str(h*d))

