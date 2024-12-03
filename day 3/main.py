# Part 1
# Logic: Use regex

import re

with open("input.txt", "r") as file:
    data = file.read().replace('\n', '')

def part1(input):
    matches = re.findall('mul\((\d+),(\d+)\)', input)
    res = 0
    for pair in matches:
        res += int(pair[0]) * int(pair[1])
    print(res)

part1(data)

# Part 2
# Logic: cut out the do and don't sections.

def part2(input):
    enabled = re.sub("don't\(\).*?do\(\)", "",input)
    part1(enabled)

part2(data)

# Note: Use the ? quantifier for less greedy regex matches. 
#       The problem I ran into was that re.sub() was too greedy in the middle .* statement.
#       This essentially meant that it would try to cut out from the first don't to the last do.