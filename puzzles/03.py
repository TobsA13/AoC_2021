from aoc import aoc

aoc = aoc(3)
lines = aoc.read_lines()


def cbits(numbers):
    r = []
    for bits in list(zip(*numbers)):
        r.append((sum(int(b) for b in bits)))
    return r


sums = cbits(lines)
mc = []
for x in sums:
    mc.append(x > len(lines) / 2)
epsilon = "".join(str(int(not x)) for x in mc)
gamma = "".join(str(int(x)) for x in mc)
print("1: ")
print(int(gamma, 2) * int(epsilon, 2))


def r(n, most=True):
    n = n.copy()
    i = 0
    while len(n) > 1:
        counts = cbits(n)
        bit = counts[i] < len(n) / 2
        if most:
            bit = not bit
        bit = int(bit)
        bit = str(bit)
        n = [n for n in n if n[i] == bit]
        i += 1
    return int(n[0], 2)


o = r(lines, True)
co2 = r(lines, False)
print("2: ")
print(o * co2)
