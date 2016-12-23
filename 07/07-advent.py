#!/usr/bin/env Python

import re
from collections import Counter

def has_abba(word):
    for index in range(len(word)-3):
        if (word[index] == word[index+3] and
            word[index+1] == word[index+2] and
            word[index] != word[index+1]):
            return True
        else:
            continue
    return False

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    with open("input.txt",'r') as f:
        lines = f.readlines()

    count = 0

    for line in lines:
        parsed_line = re.split('\W', line)
        #print parsed_line

        has_tls = False

        for index, word in enumerate(parsed_line):
            #print index, has_abba(word)

            if has_abba(word) and is_even(index):
                has_tls = True

            if has_abba(word) and not is_even(index):
                has_tls = False
                break

        if has_tls:
            count += 1

    print count

if __name__ == "__main__":
    main()