import re

with open('day05/input.txt', 'r') as f:
    lines = f.readlines()

def parse_input():
    updates = []
    rules = []

    for line in lines:
        line = line.strip()
        rule_match = re.match(r"\d+\|\d+", line)
        if rule_match is not None:
            val = line[:rule_match.start()] + line[:rule_match.end()]
            nums = tuple(map(int, val.split('|')))
            rules.append(nums)
        else:
            if len(line) != 0:
                update = list(map(int, line.split(',')))
                updates.append(update)

    return (updates, rules)

def is_correct(update: list[int], rules: list[tuple[int, int]]):
    for rule in rules:
        before_num, after_num = rule
        try:
            before_idx, after_idx = update.index(before_num), update.index(after_num)
            if before_idx > after_idx:
                return False
        except ValueError:
            pass
    return True


def sort_update(update: list[int], rules: list[tuple[int, int]]) -> bool:
    swap_made = False
    for rule in rules:
        before_num, after_num = rule
        try:
            before_idx, after_idx = update.index(before_num), update.index(after_num)
            if before_idx > after_idx:
                update[after_idx] = before_num
                update[before_idx] = after_num
                swap_made = True
        except ValueError:
            pass

    return swap_made

updates, rules = parse_input()

def part1():
    total = 0
    for update in updates:
        if is_correct(update, rules):
            total += update[len(update)//2]

    return total

def part2():
    total = 0

    for update in updates:
        swap_made = sort_update(update, rules)
        if swap_made is True:
            # keep sorting till it's correct
            while swap_made is True:
                swap_made = sort_update(update, rules)

            total += update[len(update)//2]

    return total

print("Part 1:", part1())
print("Part 2:", part2())
