#!/usr/bin/env python

with open("input.txt",'r') as f:
	lines = f.readlines()

code = []

keypad = {(-1,1): 1, (0,1): 2, (1,1): 3, (-1,0): 4, (0,0): 5,
          (1,0): 6, (-1,-1): 7, (0,-1): 8, (1,-1): 9}

x = 0
y = 0

for line in lines:
    for letter in line:
         if letter == 'L' and x > -1:
             x -= 1
         elif letter == 'R' and  x < 1:
             x += 1
         elif letter == 'U' and y < 1:
             y += 1
         elif letter == 'D' and y > -1:
             y -= 1
    code.append(keypad[(x,y)])

print "".join([str(x) for x in code] )
