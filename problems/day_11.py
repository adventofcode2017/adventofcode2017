#!/usr/bin/env python3
import argparse
import collections
import pathlib


def get_arguments():
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fp', required=True, type=pathlib.Path,
            help='Problem input filepath')

    # Validate inputs
    args = parser.parse_args()
    if not args.input_fp.exists():
        parser.error('Input file %s does not exist' % args.input_fp)

    return args


def main():
    # Get command line arguments
    args = get_arguments()

    # Read input data
    with args.input_fp.open('r') as fh:
        instructions = fh.read().rstrip().split(',')

    print('Part one:', part_one(instructions))
    print('Part two:', part_two(instructions))


def part_one(instructions):
    # Position: x, y, z
    position = [0, 0, 0]

    # Aggregate movements
    moves = collections.Counter(instructions)

    # Apply movement
    position[0] = position[0] + moves['ne'] + moves['se'] - moves['nw'] - moves['sw']
    position[1] = position[1] + moves['n'] + moves['nw'] - moves['s'] - moves['se']
    position[2] = position[2] + moves['s'] + moves['sw'] - moves['n'] - moves['ne']

    # Get distance
    distance = max((abs(n) for n in position))
    return distance


def part_two(instructions):
    # Position: x, y, z
    position = [0, 0, 0]

    # Follow movements and record distance if furthest
    max_distance = 0
    for instruction in instructions:
        # Apply move
        if instruction == 'n':
            position[1] += 1
            position[2] -= 1
        elif instruction == 'ne':
            position[0] += 1
            position[2] -= 1
        elif instruction == 'se':
            position[0] += 1
            position[1] -= 1
        elif instruction == 's':
            position[1] -= 1
            position[2] += 1
        elif instruction == 'sw':
            position[0] -= 1
            position[2] += 1
        elif instruction == 'nw':
            position[0] -= 1
            position[1] += 1
        elif instruction == 'n':
            position[1] += 1
            position[2] -= 1

        # Check if we're further than we've been
        distance = max((abs(n) for n in position))
        if distance > max_distance:
            max_distance = distance

    return max_distance


if __name__ == '__main__':
    main()
