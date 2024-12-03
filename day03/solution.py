import re


with open('day03/input.txt', 'r') as f:
    text = f.read()

def part1():
    total = 0

    for call in re.findall(r'mul\(\d+,\d+\)', text):
        n1, n2 = re.findall(r"\d+", call)
        total += (int(n1) * int(n2))

    return total

def part2():
    total = 0
    matches = re.findall(r'mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))', text)
    # find all mul(d, d) matches or don't() or do() operations
    # track these operations and track whether to compute op or not.

    compute = True
    for m in matches:
        if "don't()" in m or "do()" in m:
            compute = "do()" in m
            continue

        if compute:
            n1, n2 = tuple(filter(lambda x: x.isdigit(), m))
            total += (int(n1) * int(n2))

    return total

print("Part 1:", part1())
print("Part 2:", part2())
