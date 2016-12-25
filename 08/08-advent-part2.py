#!/usr/bin/env python

import hashlib

def brute_force_door(door_id):
    salts = map(str, range(0, 30000000))
    pw = {}

    for salt in salts:
        attempt = door_id + salt
        hashed = hashlib.md5(attempt).hexdigest()

        if hashed.startswith('00000'):
            pos = hashed[5]
            val = hashed[6]

            try:
                if int(pos) < 8 and pos not in pw:
                    pw[pos] = val
            except ValueError:
                pass

        if len(pw) == 8:
            return pw

    return pw

def main():
    door_id = 'wtnhxymk'

    ans_dict = brute_force_door(door_id)
    print ans_dict

    ans_string = ''

    for key in sorted(ans_dict):
        ans_string += ans_dict[key]

    print ans_string

if __name__ == "__main__":
    main()
