with open('day01/input.txt', 'r') as f:
    lines = f.readlines()

def part1():
    total = 0
    list1 = []
    list2 = []
    for line in lines:
        n1, n2  = map(int, line.split('   '))
        list1.append(n1)
        list2.append(n2)
        
    list1.sort()
    list2.sort()
        
    for n1, n2 in zip(list1, list2):
        total += abs(n1-n2)
        
    return total
    

def part2():
    total = 0
    list1 = []
    list2 = []
    for line in lines:
        n1, n2 = map(int, line.split('   '))
        list1.append(n1)
        list2.append(n2)
        
    list1 = set(list1)
        
    for n in list1:
        total += (n * list2.count(n))
        
    return total
    

print("Part 1:", part1())
print("Part 2:", part2())
