#!/usr/bin/env python3
import argparse
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
        instructions = [int(line.rstrip()) for line in fh]

    # Passing new list variable to avoid mutating in current scope
    print('Part one:', part_one(instructions[:]))
    print('Part two:', part_two(instructions[:]))


def part_one(instructions):
    position = 0
    steps = 0
    while True:
        try:
            value = instructions[position]
            instructions[position] += 1
            position += value
        except IndexError:
            break

        steps += 1

    return steps


def part_two(instructions):
    position = 0
    steps = 0
    while True:
        try:
            value = instructions[position]

            mod = 1 if value < 3 else -1
            instructions[position] += mod

            position += value
        except IndexError:
            break

        steps += 1

    return steps


if __name__ == '__main__':
    main()
