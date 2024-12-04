# Part 1

#
# Logic: Locate every X in the text. Go in a circle around each X to try and complete the word XMAS
# Initialize data as an array 

import numpy as np

text = open("input.txt", "r")
data = []
for line in text:
    lineArr = []
    for char in line:
        if char == "\n":
            continue
        lineArr.append(char)
    data.append(lineArr)

def getDiagonals(arr):
    res = []
    for i in range(len(arr)):
        res.append(np.diagonal(arr, i).tolist())
        if i != 0: res.append(np.diagonal(arr, i*-1).tolist())
    return res

def search(arr):
    res = 0
    for line in arr:
        if len(line) < 4:
            continue
        print(line)
        for char in range(len(line) - 3):
            if line[char] == "X" and line[char + 1] == "M" and line[char + 2] == "A" and line[char + 3] == "S":
                res += 1
            elif line[char] == "S" and line[char + 1] == "A" and line[char + 2] == "M" and line[char + 3] == "X":
                res += 1
            else:
                continue
    return res

def part2():
    dataArr = np.array(data)
    dataArrCol = np.transpose(dataArr)
    diagonals = getDiagonals(dataArr)
    diagonalsFlipped = np.fliplr(dataArr)
    res = search(dataArr) + search(dataArrCol) + search(diagonals) + search(diagonalsFlipped)
    return res

print(part2())