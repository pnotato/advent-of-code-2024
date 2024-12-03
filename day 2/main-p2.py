# OK I ended up brute forcing the solution. May revisit this problem.

# Logic: Check for a directional change with each number. keep track of ups and downs. 
#        if the list is going one direction, there should be at most 1 of the other direction
#        to account for the dampener.
#
#   e.g. [1, 5, 4, 3, 2] goes up, down, down, down, which is safe. 
#   e.g. [1, 3, 2, 4, 5] goes up, down, up, up, which is safe. 
#   e.g. [5, 4, 2, 3, 6] goes down, down, up, up, which is not safe

# Logic: Verify if the list follows the rules. If it's not safe, find the first offender.
# If the list is still not safe, then don't add to res.

# Note: use reverse in sorted.
def verify(values):
    if (values == sorted(values) or values == sorted(values, reverse=True)):
        for i in range(len(values)-1):
            if 1 <= abs(values[i] - values[i+1]) <= 3:
                continue
            else:
                return False
        return True
    return False
    
def part2():
    input = open("input.txt", "r")
    res = 0
    for line in input:
        lines = line.split(" ")
        values = list(map(int, lines))
        if verify(values):
            res += 1
        else:
            for i in range(len(values)):
                new = values[:i] + values[i+1:]
                if verify(new):
                    res += 1
                    break
    print(res)

part2()


# def CountDirectionals(values):
#     up, down = 0, 0
#     for i in range(len(values)-1):
#         if values[i] < values[i+1]:
#             up += 1
#         elif values[i] > values[i+1]:
#             down += 1
#         if up > 0 and down > 0:
#             return i
#     return 9999

# def CountGaps(values):
#     gaps = []
#     for i in range(len(values)-1):
#         gaps.append(abs(values[i] - values[i+1]))
#     for i, gap in enumerate(gaps):
#         if gap < 1 or gap > 3:
#             return i
#     return 9999

