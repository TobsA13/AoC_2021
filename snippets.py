print("Enter/Paste your content. Ctrl-D to save it.")
print()
contents = []
while True:
    try:
        line = input("")
    except EOFError:
        break
    if line.strip():
        contents.append(line)



f = open("file", "r")
data = f.readlines()