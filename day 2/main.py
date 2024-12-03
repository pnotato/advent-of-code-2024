# Logic: Check for a directional change with each number. keep track of ups and downs. 
#        if the list is going one direction, there should be at most 1 of the other direction
#        to account for the dampener.
#
#   e.g. [1, 5, 4, 3, 2] goes up, down, down, down, which is safe. 
#   e.g. [1, 3, 2, 4, 5] goes up, down, up, up, which is safe. 
#   e.g. [5, 4, 2, 3, 6] goes down, down, up, up, which is not safe

# With the same idea, create a list of the differences between the numbers
#   e.g. [1, 5, 4, 3, 2] goes 4, 1, 1, 1, which is safe
#   e.g. [1, 3, 2, 4, 5] goes 2, 1, 2, 1, which is safe
#   e.g. [5, 4, 2, 3, 7] goes 1, 2, 1, 4, which is not safe

# and then just && the values together.

def CountDirectionals(values):
    up, down = 0, 0
    for i in range(len(values)-1):
        if values[i] < values[i+1]:
            up += 1
        elif values[i] == values[i+1]:
            return False
        else:
            down += 1
    return up == 0 or down == 0

def CountGaps(values):
    gaps = []
    for i in range(len(values)-1):
        gaps.append(abs(values[i] - values[i+1]))
    for j in gaps:
        if j < 1 or j > 3:
            return False
        else: 
            continue
    return True

def part2():
    input = open("input.txt", "r")
    res = 0
    for line in input:
        lines = line.split(" ")
        values = list(map(int, lines))
        if CountDirectionals(values) and CountGaps(values):
            res += 1

    print(res)

part2()