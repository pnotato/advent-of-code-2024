# Part 1
# Logic: 
#   adjacent levels can differ by at most 3 and at least 1. the first and last number
#   should be be between 3*amount of numbers-1 numbers different. 
#
#   if the line isn't the same as the sorted version of the line, return false

def loopOverRange(values):
    Valuerange = len(values) - 1
    for i in range(Valuerange):
        if 1 <= abs(values[i] - values[i+1]) <= 3:
            continue
        else:
             return False
    return True



def part1():
    input = open("input.txt", "r")
    res = 0
    for line in input:
        lines = line.split(" ")
        values = list(map(int, lines))
        valueSorted = sorted(values)
        if (values == valueSorted or list(reversed(values)) == valueSorted) and valueSorted[0] >= valueSorted[-1] - 3*(len(valueSorted)-1) and loopOverRange(values):
            # Note: reversed returns an iterator, not a list. 
            res += 1
        else:
            continue
    print(res)

part1()

