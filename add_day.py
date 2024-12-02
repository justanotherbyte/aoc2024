import os
import sys

import requests


PY_TEMPLATE = """with open('{}/input.txt', 'r') as f:
    lines = f.readlines()

def part1():
    ...

def part2():
    ...

print("Part 1:", part1())
print("Part 2:", part2())
"""

CPP_TEMPLATE = """#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int part1() {
    ifstream f("<DIRNAME>/input.txt");

    string line;
    while (getline(f, line)) {
        // do something...
    }
}

int part2() {
    ifstream f("<DIRNAME>/input.txt");

    string line;
    while (getline(f, line)) {
        // do something...
    }
}

int main() {
    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
}
"""


def download(day: str) -> bytes:
    with open(".session", "r") as f:
        session = f.read().strip()

    cookies = {"session": session}
    resp = requests.get(
        f"https://adventofcode.com/2024/day/{day}/input", cookies=cookies)
    resp.raise_for_status()

    return resp.content


def setup(day: str) -> None:
    puzzle_input = download(day)
    dirname = "day{:02}".format(int(day))
    os.mkdir(dirname)
    os.chdir(dirname)

    with open("solution.py", "w") as f:
        f.write(PY_TEMPLATE.format(dirname))

    with open("solution.cpp", "w") as f:
        f.write(CPP_TEMPLATE.replace("<DIRNAME>", dirname))

    with open("input.txt", "wb") as f:
        f.write(puzzle_input)  # type: ignore

    with open("example.txt", "w") as _:
        pass


day = sys.argv[-1]
setup(day)
print("Setup complete...")
