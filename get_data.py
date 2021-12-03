from datetime import datetime

import requests
import os

day = datetime.today().day

headers = {'session': os.environ['AOC_SESSION']}
url = f'https://adventofcode.com/2021/day/{day}/input'

session = requests.Session()
resp = session.get(url, cookies=headers)

lines = resp.text.split("\n")
if lines[len(lines) - 1].strip() == "":
    lines.pop()

in_file = open(f'inputs/{day}', 'w')
in_file.write("\n".join(lines))
in_file.close()
