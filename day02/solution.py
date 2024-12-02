with open('day02/input.txt', 'r') as f:
    lines = f.readlines()

def is_safe(nums: list[int]) -> bool:
    if sorted(nums) == nums or sorted(nums, reverse=True) == nums:
        differs = []
        for i in range(len(nums)-1):
            n1 = nums[i]
            n2 = nums[i+1]
            differs.append(abs(n1-n2))

        if (differs.count(1) + differs.count(2) + differs.count(3)) == len(differs):
            return True

    return False

def part1():
    safe = 0
    for line in lines:
        nums = list(map(int, line.split(' ')))
        if is_safe(nums):
            safe += 1

    return safe

def part2():
    safe = 0
    for line in lines:
        nums = list(map(int, line.split(' ')))
        for n in nums:
            nums_new = nums.copy()
            nums_new.remove(n)
            if is_safe(nums_new):
                safe += 1
                break

    return safe

print("Part 1:", part1())
print("Part 2:", part2())
