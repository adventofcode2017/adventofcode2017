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
        data = fh.read().rstrip()

    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


def hash_round(numbers, lengths, skip, offset):
    for length in lengths:
        # Reverse slice and reconstruct number list
        numbers = numbers[:length][::-1] + numbers[length:]

        # Always rotate such that current position is at list index zero
        distance = (length + skip) % len(numbers)
        numbers = numbers[distance:] + numbers[:distance]

        # Track rotations so we can locate 'start' of list; inc skip distance
        offset += distance
        skip += 1

    return numbers, skip, offset


def block_xor(block):
    # Return variable
    result = 0
    for number in block:
        result ^= number
    return result


def part_one(data, numbers=list(range(256))):
    # Init variables
    lengths = [int(l) for l in data.split(',')]

    # Call single round of hash function
    numbers, skip, offset = hash_round(numbers, lengths, 0, 0)

    # Multiply first and second elements from 'start' of list
    start_index = len(numbers) - (offset % len(numbers))
    return numbers[start_index] * numbers[start_index+1]


def part_two(data):
    # Init variables
    lengths = [ord(c) for c in data]
    lengths.extend([17, 31, 73, 47, 23])
    numbers = list(range(256))

    # Calculate sparse hash
    skip = 0
    offset = 0
    for i in range(64):
        numbers, skip, offset = hash_round(numbers, lengths, skip, offset)

    # Rotate numbers to list 'start'
    start_index = len(numbers) - (offset % len(numbers))
    numbers = numbers[start_index:] + numbers[:start_index]

    # Calculate dense hash
    block_gen = (numbers[i:i+16] for i in range(0, len(numbers), 16))
    dense_hash = [block_xor(block) for block in block_gen]

    # Return hex repr
    return ''.join(('{:02x}'.format(h) for h in dense_hash))


if __name__ == '__main__':
    main()
