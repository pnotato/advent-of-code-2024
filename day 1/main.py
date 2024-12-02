# Part 1
# Logic: Sort both lists and iterate through them to find the difference.

def readfile():
    input = open("input.txt", "r")
    right = []
    left = []
    for line in input:
        values = line.split("  ")
        left.append(int(values[0]))
        right.append(int(values[1].strip()))
    return right, left

def part1():
    right, left = readfile()
    sortedright = sorted(right)
    sortedleft = sorted(left)   
    res = 0
    for i in range(len(left)):
        res += abs(sortedright[i] - sortedleft[i])
    print(res)

part1()

# Part 2
# Logic: Use a Hash map.

def part2():
    right, left = readfile()
    reslist = {}
    res = 0
    for number in right:
        if reslist.get(number): 
            reslist[number] += 1
        else: 
            reslist[number] = 1
    for number in left:
        if not reslist.get(number): continue
        res += reslist[number] * number

    print(res)

part2()