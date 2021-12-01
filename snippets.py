# Strip elements of list
lines = map(lambda x: x.strip(), lines)

# Remove empty strings in list
lines = filter(lambda x: x != '', lines)

# Convert every element in list to int
lines = list(map(lambda x: int(x), lines))
