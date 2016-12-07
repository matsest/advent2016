#!/usr/bin/env python

with open("input.txt",'r') as f:
    lines = f.readlines()

count = 0
	
for line in lines:
    numbers = [int(num) for num in line.split()]
    numbers = sorted(numbers)

    if (numbers[0] + numbers[1]) > numbers [2]:
        count += 1
    else:
        continue

print count
