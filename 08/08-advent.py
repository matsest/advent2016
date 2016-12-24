#!/usr/bin/env Python

import hashlib

def brute_force_next(door_id):

    salts = map(str, range(0, 10000000))
    pw = ''
    for salt in salts:
        attempt = door_id + salt
        hashed = hashlib.md5(attempt).hexdigest()

        if hashed.startswith('00000'):
            pw += hashed[5]
            if len(pw) > 7:
                break
    return pw

def main():
    door_id = 'wtnhxymk'

    print brute_force_next(door_id)

if __name__ == "__main__":
    main()