#!/usr/bin/env python

# Read file and numbers as rows
with open("input.txt",'r') as f:
    lines = f.readlines()

rows = []
for line in lines:
    numbers = [int(num) for num in line.split()]
    rows.append(numbers)

max_range = len(lines)

# Make empty columns
cols = [[] for i in range(max_range)]
index = 0

# Traverse columns by 3 and 3 
for i in xrange(0,max_range,3):
    for j in range(3):
        cols[index] = [rows[i][j], rows[i+1][j], rows[i+2][j]]
        index += 1

# Find numbers of valid triangles:
count = 0

for line in cols:
    numbers = sorted(line)

    if (numbers[0] + numbers[1]) > numbers [2]:
        count += 1
    else:
        continue

print count
