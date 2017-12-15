#!/usr/bin/env python3
import argparse
import pathlib


# Handling relative imports for unittest
try:
    import day_10
except ModuleNotFoundError:
    from problems import day_10


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
        hash_input = fh.read().rstrip()

    print('Part one:', part_one(hash_input))
    print('Part two:', part_two(hash_input))


def get_disk_status(hash_input):
    rows = list()
    for n in range(128):
        # Run knot hash
        row_hash = '%s-%s' % (hash_input, n)
        hex_repr = day_10.part_two(row_hash)

        # Conver to binary representation of row and record
        bin_repr = ''.join((format(int(h, 16), '04b') for h in hex_repr))
        rows.append(bin_repr)
    return rows


def process_group(disk_grid, i, j):
    group_stack = [(i, j)]
    while group_stack:
        # Pop from top of stack and set position value to zero
        i, j = group_stack.pop()
        disk_grid[j][i] = 0

        # Discover adjacent group members
        for ai, aj in adjacent_orthogonal_positions(i, j):
            # Check that we remain in quad 1
            if ai < 0 or aj < 0:
                continue

            # Check we remain within bounds of grid
            if ai >= len(disk_grid) or aj >= len(disk_grid):
                continue

            if disk_grid[aj][ai] == '1':
                group_stack.append((ai, aj))


def adjacent_orthogonal_positions(i, j):
    for position in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        yield position


def part_one(hash_input):
    return sum((row.count('1') for row in get_disk_status(hash_input)))


def part_two(hash_input):
    group_count = 0
    disk_grid = [list(row) for row in get_disk_status(hash_input)]

    for j, row in enumerate(disk_grid):
        for i, element in enumerate(row):
            if element == '1':
                group_count += 1
                process_group(disk_grid, i, j)

    return group_count


if __name__ == '__main__':
    main()
