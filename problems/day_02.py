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
        row_gen = (line.rstrip().split('\t') for line in fh)
        rows = [[int(c) for c in row] for row in row_gen]

    print('Part one:', part_one(rows))
    print('Part two:', part_two(rows))


def part_one(rows):
    checksum = 0
    for row in rows:
        checksum += (max(row) - min(row))

    return checksum


def part_two(rows):
    div_sum = 0
    for row in rows:
        row_ordered = sorted(row, reverse=True)
        for i in range(len(row_ordered)):
            for j in range(i+1, len(row_ordered)):
                if row_ordered[i] % row_ordered[j] == 0:
                    div_sum += (row_ordered[i] // row_ordered[j])
    return div_sum


if __name__ == '__main__':
    main()
