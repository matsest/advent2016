#!/usr/bin/env Python
'''Based on solution by Reibello from reddit: http://pastebin.com/5rBU4nYR'''

import re

def get_abas(word):
    abas = []
    for i in range(len(word) - 2):
        three_next = word[i:i+3]
        if (three_next[0] == three_next[2] and
            three_next[0] != three_next[1]):
            abas.append(three_next)
    return abas

def support_ssl(addr):
    regex = re.compile(r'.*\[([a-z]+)\].*')
    hypernets = []
    while True:
        matched = regex.match(addr)
        if not matched:
            break
        inner = matched.groups()[0]
        hypernets.append(inner)
        addr = addr.replace(inner, '')

    abas = get_abas(addr)
    for aba in abas:
        bab = ''.join([aba[1], aba[0], aba[1]])
        for hyper in hypernets:
            if bab in hyper:
                return True
    return False

def main():
    with open("input.txt",'r') as f:
        lines = f.readlines()

    count = 0

    for line in lines:
        if support_ssl(line):
            count += 1
    print "Total count: ", count

if __name__ == "__main__":
    main()
