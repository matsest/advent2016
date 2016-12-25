#!/usr/bin/env python

class Player:
    def __init__(self):
        self.position = [0, 0]
        self.current_dir_id = 0

    def change_direction(self, new_direction):
        if new_direction == 'L':
            new_dir_id = (self.current_dir_id - 1) % 4
        elif new_direction == 'R':
            new_dir_id = (self.current_dir_id + 1) % 4
        self.current_dir_id = new_dir_id

    def move(self, direction, length):
        x = self.position[0]
        y = self.position[1]

        if direction == 0:
            y += length
        elif direction == 1:
            x += length
        elif direction == 2:
            y -= length
        elif direction == 3:
            x -= length
        self.position = [x, y]

def main():
    with open("input.txt", 'r') as f:
        dirs = f.read()

    directions = ['N', 'E', 'S', 'W']

    santas_helper = Player()

    visited = [santas_helper.position]

    print "Starting to find Easter Bunny HQ:"
    print "Current direction: ", directions[santas_helper.current_dir_id]
    print "Current position: ", santas_helper.position
    print "\n"
    counter = 1

    for direction in dirs.strip().split(', '):
        rot = direction[0]
        length = int(direction[1:])
        print 'Direction #', counter
        counter += 1
        print 'Rotate: ', rot, ' Length: ', length

        santas_helper.change_direction(rot)
        print "Current direction: ", directions[santas_helper.current_dir_id]

        for _ in range(length):
            santas_helper.move(santas_helper.current_dir_id, 1)

            print "Current position: ", santas_helper.position

            if santas_helper.position not in visited:
                visited.append(santas_helper.position)
            else:
                print '\nVisited twice!'
                print "Length from start: ", (abs(santas_helper.position[0]) +
                                              abs(santas_helper.position[1]))

                return

        print "\n"

if __name__ == "__main__":
    main()
