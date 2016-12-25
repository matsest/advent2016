#!/usr/bin/env python

import re
from collections import Counter


def main():
    with open("input.txt", 'r') as fil:
        lines = fil.readlines()

    sector_id_sum = 0

    # Sample line:
    # jchipqat-uadltg-hidgpvt-375[kcnop]
    for line in lines:
        parsed_line = re.sub('-', '', line)
        parsed_line = re.split(r'(\d+)', parsed_line)
        parsed_line[-1] = parsed_line[-1].strip('[]\n')

        encrypted = parsed_line[0]
        sector_id = int(parsed_line[1])
        checksum = parsed_line[2]

        counter = Counter(encrypted)
        most_common = sorted(counter.items(), key=lambda pair: (-pair[1], pair[0]))

        counts = most_common[:len(checksum)]

        test_word = ''
        for count in counts:
            test_word += count[0]

        if test_word == checksum:
            sector_id_sum += sector_id

    print "Sector ID sum:", sector_id_sum

if __name__ == "__main__":
    main()
