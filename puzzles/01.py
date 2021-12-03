from pprint import pprint

print("AoC 2021-01")
print()

f = open("../inputs/01data", "r")
data = f.readlines()

#------------- Part 1

count = 0
old_count = 0

for i, d in enumerate(data):
    if i == 0:
        continue
    if int(d) > old_count:
        count += 1
    old_count = int(d)

print("Result: " + str(count))

#------------- Part 2

cleanData = []
for i in range(len(data)):
    if len(data) - 2 == i:
        break
    cleanData.append(int(data[i]) + int(data[i + 1]) + int(data[i + 2]))

count = 0
old_count = 0

for i, d in enumerate(cleanData):
    if i == 0:
        continue
    if int(d) > old_count:
        count += 1
    old_count = int(d)

print("Result 2: " + str(count))