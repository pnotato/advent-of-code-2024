# Part 1

def verify(values):
    if (values == sorted(values) or list(reversed(values)) == sorted(values)):
        for i in range(len(values)-1):
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
        if verify(values):
            res += 1
    print(res)

part1()
    