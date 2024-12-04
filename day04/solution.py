with open('day04/input.txt', 'r') as f:
    lines = f.readlines()

def read_direction(
    target: str,
    direction: tuple[int, int],
    current_pos: tuple[int, int],
    bounds: tuple[int, int]
) -> list[str] | None:
    x, y = current_pos
    dx, dy = direction
    bounds_x, bounds_y = bounds

    # check bounds
    final_x = x + (dx * (len(target)-1))
    final_y = y + (dy * (len(target)-1))

    if (final_x in range(0, bounds_x)) and (final_y in range(0, bounds_y)):
        chars = []

        for i in range(len(target)):
            pos_x = x + (i * dx)
            pos_y = y + (i * dy)

            chars.append(lines[pos_y][pos_x])

        return chars

    return None # not in bounds


def part1():
    total = 0

    directions = [
        (0, 1), # below
        (0, -1), # above
        (-1, 1), # below left
        (-1, -1), # above left
        (1, -1), # above right
        (1, 1) # below right
    ]

    target = "XMAS"
    for row_idx, row in enumerate(lines):
        row = row.strip()
        total += row.count(target)
        total += row.count(target[::-1])

        for char_idx, char in enumerate(row):
            if char == "X":
                for direction in directions:
                    chars = read_direction(
                        target,
                        direction,
                        (char_idx, row_idx),
                        (len(row), len(lines))
                    )

                    if chars is not None:
                        joined = ''.join(chars)
                        if joined == target:
                            total += 1
    return total


def part2():
    total = 0

    dpairs = [
        ((-1, 1), (1, -1)), # pair1: below left above right,
        ((1, 1), (-1, -1)) # pair2: below right above left
    ]

    target = "AA" # generic 2 letter target

    for row_idx, row in enumerate(lines):
        row = row.strip()
        for char_idx, char in enumerate(row):
            if char == "A":
                count = True
                for (below, upper) in dpairs:
                    chars1 = read_direction(
                        target,
                        below,
                        (char_idx, row_idx),
                        (len(row), len(lines))
                    )
                    chars2 = read_direction(
                        target,
                        upper,
                        (char_idx, row_idx),
                        (len(row), len(lines))
                    )

                    if chars1 and chars2:
                        l1, l2 = chars1[1], chars2[1]
                        cset = {"S", "M"}

                        if (l1 != l2) and (l1 in cset) and (l2 in cset):
                            continue
                        else:
                            count = False
                    else:
                        count = False

                if count is True:
                    total += 1

    return total


print("Part 1:", part1())
print("Part 2:", part2())
