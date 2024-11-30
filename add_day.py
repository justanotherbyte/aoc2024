import os
import sys

import requests


DAY_TEMPLATE = """with open('{}/input.txt', 'r') as f:
    lines = f.readlines()

def part1():
    ...

def part2():
    ...

print('Part 1:', part1())
print('Part 2:', part2())
"""

def download(day: str) -> bytes:
    with open(".session", "r") as f:
        session = f.read().strip()

    cookies = {"session": session}
    resp = requests.get(f"https://adventofcode.com/2024/day/{day}/input", cookies=cookies)
    resp.raise_for_status()

    return resp.content

def setup(day: str) -> None:
    dirname = f"day{day}"
    os.mkdir(dirname)
    os.chdir(dirname)

    with open("solution.py", "w") as f:
        f.write(DAY_TEMPLATE.format(dirname))

    problem_input = b"TEST"
    with open("input.txt", "wb") as f:
        f.write(problem_input) # type: ignore

day = sys.argv[-1]
setup(day)
