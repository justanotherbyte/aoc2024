import re
import itertools


with open("day07/input.txt", "r") as f:
    lines = f.readlines()

def parse_equations():
    equations = {}
    for line in lines:
        line = line.strip()
        nums = list(map(int, re.findall(r"\d+", line)))
        equations[nums[0]] = nums[1:]

    return equations

equations = parse_equations()
operations = [
    lambda x, y: x + y,
    lambda x, y: x * y
]

def compute_operation(
    nums: list[int],
    ops: list
):
    ops = iter(ops) # type: ignore
    op = next(ops)
    ans = op(nums[0], nums[1])

    for i in range(2, len(nums)):
        op = next(ops) # type: ignore
        ans = op(ans, nums[i])

    return ans

def part1():
    total = 0
    for result, nums in equations.items():
        for perm in itertools.product(operations, repeat=len(nums)-1):
            if compute_operation(nums, perm) == result:
                total += result
                break

    return total


def part2():
    operations.append(
        lambda x, y: int(f"{x}{y}")
    )
    return part1()

print("Part 1:", part1())
print("Part 2:", part2())
