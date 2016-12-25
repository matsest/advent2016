#!/usr/bin/env python

from collections import Counter

def main():

	with open("input.txt",'r') as f:
		lines = f.readlines()

	WIDTH = len(lines[0])

	cols = [[] for i in range(WIDTH)]
	print cols

	for line in lines:
		for i in range(WIDTH):
			cols[i].append(line[i])

	for col in cols:
		print Counter(col).most_common(1)[0][0]

if __name__ == "__main__":
    main()
