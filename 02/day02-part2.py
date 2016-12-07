#!/usr/bin/env python

with open("input.txt",'r') as f:
	lines = f.readlines()

code = []

keypad = {(-1,1): 2, (0,1): 3, (1,1): 4, (-1,0): 6, (0,0): 7,
          (1,0): 8, (-1,-1): 'A', (0,-1): 'B', (1,-1): 'C', (0,-2): 'D', (0,2): 1, (2,0): 9, (-2,0): 5}

(x,y) = keypad.keys()[keypad.values().index(5)] 

for line in lines:
    for letter in line:
        if letter == 'L' and ((x > -1 and abs(y) < 2) or (x,y) == (-1,0)):
            x -= 1
        elif letter == 'R' and  ((x < 1 and abs(y) < 2) or (x,y) == (1,0)):
            x += 1
        elif letter == 'U' and ((y < 1 and abs(x) < 2) or (x,y) == (0,1)):
            y += 1
        elif letter == 'D' and ((y > -1 and abs(x) < 2) or (x,y) == (0,-1)):
            y -= 1

    code.append(keypad[(x,y)])

print "".join([str(x) for x in code] )