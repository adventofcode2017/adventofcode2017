#!/usr/bin/env python3
import argparse
import pathlib
import re


garbage_can_re = re.compile(r'(!.)')
garbage_re = re.compile(r'(<.*?>)')
group_re = re.compile


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
        stream = fh.read().rstrip()

    print('Part one:', part_one(stream))
    print('Part two:', part_two(stream))


def part_one(stream):
    # Remove cancelled characters and then garbage
    stream = garbage_can_re.sub('', stream)
    stream = garbage_re.sub('', stream)

    # Process groups and calculate score
    depth = 0
    score = 0
    for c in stream:
        if c == '{':
            depth += 1
            score += depth
        elif c == '}':
            depth -= 1
        elif c == ',':
            pass

    # Check that all groups were correctly terminated
    assert depth == 0

    return score


def part_two(stream):
    # Remove cancelled characters and collect the garbage
    stream = garbage_can_re.sub('', stream)
    garbage_bins = garbage_re.findall(stream)

    # Count the garbage
    garbage_chars = sum((len(b) for b in garbage_bins)) - (2 * len(garbage_bins))

    return garbage_chars


if __name__ == '__main__':
    main()
