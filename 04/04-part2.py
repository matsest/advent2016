#!/usr/bin/env Python

import re
import string
from collections import Counter

def rotate(myList, n):

	if n > len(myList):
		n = n % len(myList)

	return myList[n:] + myList[:n]

def main():

	with open("input.txt",'r') as f:
		lines = f.readlines()

	sector_id_sum = 0

	# Sample line:
	# qzmt-zixmtkozy-ivhz-343
	for line in lines:
		parsed_line = re.sub('-',' ',line)
		parsed_line = re.split('(\d+)', parsed_line)
		parsed_line[-1] = parsed_line[-1].strip('[]\n')

		encrypted = parsed_line[0]
		sector_id = int(parsed_line[1])
		checksum = parsed_line[2]

		alphs = list(string.ascii_lowercase)
		newalphs = rotate(alphs,sector_id)

		cipher = dict(zip(alphs,newalphs))

		real = ''
		for c in encrypted:
			if c == ' ':
				real += c
			else:
				real += cipher[c]

		if re.search('north', real):
			print real, sector_id

if __name__ == "__main__":
    main()
