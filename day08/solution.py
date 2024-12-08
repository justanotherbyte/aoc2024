import itertools

with open('day08/input.txt', 'r') as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]

def find_frequencies():
    freqs = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                current_points = freqs.get(grid[r][c]) or []
                current_points.append((r, c))
                freqs[grid[r][c]] = current_points

    return freqs

def is_bounds(pos: tuple[int, int], grid: list[list[str]]):
    r, c = pos
    return r in range(len(grid)) and c in range(len(grid[0]))


def part1():
    freqs = find_frequencies()
    antinodes = set()
    for freq, positions in freqs.items():
        for (r1, c1), (r2, c2) in itertools.combinations(positions, r=2):
            dr = r1 - r2
            dc = c1 - c2

            antinode1 = (r1 - (2*dr)), (c1 - (2*dc))
            antinode2 = (r1 + dr), (c1 + dc)

            if is_bounds(antinode1, grid):
                antinodes.add(antinode1)

            if is_bounds(antinode2, grid):
                antinodes.add(antinode2)

    return len(antinodes)

is_antenna = lambda pos: grid[pos[0]][pos[1]] != "."

def part2():
    freqs = find_frequencies()
    antinodes = set()
    for freq, positions in freqs.items():
        for (r1, c1), (r2, c2) in itertools.combinations(positions, r=2):
            dr = r1 - r2
            dc = c1 - c2

            antinode1 = (r1 - (2*dr)), (c1 - (2*dc))
            antinode2 = (r1 + dr), (c1 + dc)

            while is_bounds(antinode1, grid):
                if not is_antenna(antinode1):
                    antinodes.add(antinode1)
                ra, ca = antinode1
                antinode1 = (ra - dr), (ca - dc)

            while is_bounds(antinode2, grid):
                if not is_antenna(antinode2):
                    antinodes.add(antinode2)
                ra, ca = antinode2
                antinode2 = (ra + dr), (ca + dc)

    total = len(antinodes)
    total += sum(len(p) for p in freqs.values())
    return total

print("Part 1:", part1())
print("Part 2:", part2())
