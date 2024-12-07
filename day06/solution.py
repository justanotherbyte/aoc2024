import itertools

with open("day06/input.txt", "r") as f:
    lines = f.readlines()


grid = [list(line.strip()) for line in lines]

def get_directions():
    ds = ((-1, 0), (0, 1), (1, 0), (0, -1))
    return itertools.cycle(ds)

def part1():
    guard_pos = (0, 0) # placeholder
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] not in {".", "#"}:
                guard_pos = (r, c)

    directions = get_directions()
    direction = next(directions)

    positions = {guard_pos,}

    traversed = False
    while not traversed:
        found_obstacle = False
        while not found_obstacle:
            nr, nc = new_pos = (
                guard_pos[0] + direction[0],
                guard_pos[1] + direction[1]
            )
            if (nr not in range(len(grid))) or (nc not in range(len(grid[0]))):
                traversed = True
                break
            if grid[nr][nc] == "#":
                found_obstacle=True
                direction = next(directions)
                break
            else:
                positions.add(new_pos)
                guard_pos = new_pos

    return len(set(positions))

def part2():
    total = 0
    guard_pos = (0, 0) # placeholder
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] not in {".", "#"}:
                guard_pos = (r, c)

    OG_guard_pos = guard_pos

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "^":
                continue

            old_char = grid[r][c]
            grid[r][c] = "#"
            directions = get_directions()
            direction = next(directions)

            positions = {(guard_pos, direction)}

            traversed = False
            while not traversed:
                found_obstacle = False
                while not found_obstacle:
                    nr, nc = new_pos = (
                        guard_pos[0] + direction[0],
                        guard_pos[1] + direction[1]
                    )
                    if (nr not in range(len(grid))) or (nc not in range(len(grid[0]))):
                        traversed = True
                        break
                    if grid[nr][nc] == "#":
                        found_obstacle=True
                        direction = next(directions)
                        break
                    else:
                        if (new_pos, direction) in positions:
                            total += 1
                            traversed = True
                            break
                        positions.add((new_pos, direction))
                        guard_pos = new_pos

            grid[r][c] = old_char
            guard_pos = OG_guard_pos

    return total


print("Part 1:", part1())
print("Part 2:", part2())
