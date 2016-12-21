#!/usr/bin/env Python

import re
import string


def rotate(my_list, n):
    if n > len(my_list):
        n = n % len(my_list)

    return my_list[n:] + my_list[:n]


def main():
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    # Sample line:
    # qzmt-zixmtkozy-ivhz-343
    for line in lines:
        parsed_line = re.sub('-', ' ', line)
        parsed_line = re.split(r'(\d+)', parsed_line)
        parsed_line[-1] = parsed_line[-1].strip('[]\n')

        encrypted = parsed_line[0]
        sector_id = int(parsed_line[1])

        alphs = list(string.ascii_lowercase)
        newalphs = rotate(alphs, sector_id)

        cipher = dict(zip(alphs, newalphs))

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
