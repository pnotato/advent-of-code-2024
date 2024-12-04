# Part 1

#
# Logic: Locate every X in the text. Go in a circle around each X to try and complete the word XMAS
# Initialize data as an array 

import numpy as np

# Read and process the input file
with open("input.txt", "r") as text:
    data = []
    for line in text:
        lineArr = []
        for char in line:
            if char == "\n":
                continue
            lineArr.append(char)
        data.append(lineArr)

max_length = max(len(row) for row in data)

# Pad shorter rows with spaces to match the maximum length
for row in data:
    if len(row) < max_length:
        row.extend([' '] * (max_length - len(row)))

def getDiagonals(arr):
    res = []
    for i in range(len(arr)):
        diag = np.diagonal(arr, offset=i).tolist()
        res.append(diag)
        if i != 0:
            diag_neg = np.diagonal(arr, offset=-i).tolist()
            res.append(diag_neg)
    return res

def search(arr):
    res = 0
    for line in arr:
        if len(line) < 4:
            continue
        for char in range(len(line) - 3):
            # Check for "XMAS"
            if (line[char] == "X" and line[char + 1] == "M" and
                line[char + 2] == "A" and line[char + 3] == "S"):
                res += 1
            # Check for "SAMX"
            elif (line[char] == "S" and line[char + 1] == "A" and
                  line[char + 2] == "M" and line[char + 3] == "X"):
                res += 1
    return res

def part2():
    dataArr = np.array(data)
    dataArrCol = np.transpose(dataArr)
    diagonals = getDiagonals(dataArr)
    flippedArr = np.fliplr(dataArr)
    diagonalsFlipped = getDiagonals(flippedArr)
    return (search(dataArr.tolist()) +
            search(dataArrCol.tolist()) +
            search(diagonals) +
            search(diagonalsFlipped))

# Execute the main function and print the result
print(part2())
