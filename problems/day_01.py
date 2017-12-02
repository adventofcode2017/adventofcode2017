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
        digits = [int(d) for d in fh.read().rstrip()]

    # Create copies of lists to avoid unwanted modification
    print('Part one:', part_one(digits[:]))
    print('Part two:', part_two(digits[:]))


def part_one(digits):
    # Return variable
    sequence_sum = 0

    # First process end->first pair
    first_digit = digits.pop(0)
    if first_digit == digits[-1]:
        sequence_sum += first_digit

    # Process remaining
    previous_digit = first_digit
    for digit in digits:
        if previous_digit == digit:
            sequence_sum += digit
            continue

        # Update previous digit
        previous_digit = digit

    return sequence_sum


def part_two(digits):
    # Return variable
    sequence_sum = 0

    pair_offset = len(digits) // 2
    for i, digit in enumerate(digits):
        pair_idx = (pair_offset + i) % len(digits)
        if digit == digits[pair_idx]:
            sequence_sum += digit

    return sequence_sum


if __name__ == '__main__':
    main()
