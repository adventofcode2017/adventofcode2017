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
        bank_config = [int(b) for b in fh.readline().rstrip().split()]

    # Passing new list variable to avoid mutating in current scope
    print('Part one:', part_one(bank_config[:]))
    print('Part two:', part_two(bank_config[:]))


def part_one(bank_config):
    redis_count = 0
    seen_bank_configs = set()
    while tuple(bank_config) not in seen_bank_configs:
        # Record current bank config
        seen_bank_configs.add(tuple(bank_config))

        # Find bank with highest block count
        banks_sorted = sorted(enumerate(bank_config), key=lambda k: k[1], reverse=True)
        bank_idx, block_count = banks_sorted[0]

        # Redistribute
        bank_config[bank_idx] = 0
        while block_count:
            bank_idx = (bank_idx + 1) % len(bank_config)
            block_count -= 1
            bank_config[bank_idx] += 1

        # Count redistribution
        redis_count += 1

    return redis_count


def part_two(bank_config):
    redis_count = 0
    seen_bank_configs = dict()
    while tuple(bank_config) not in seen_bank_configs:
        # Record current bank config
        seen_bank_configs[tuple(bank_config)] = redis_count

        # Find bank with highest block count
        banks_sorted = sorted(enumerate(bank_config), key=lambda k: k[1], reverse=True)
        bank_idx, block_count = banks_sorted[0]

        # Redistribute
        bank_config[bank_idx] = 0
        while block_count:
            bank_idx = (bank_idx + 1) % len(bank_config)
            block_count -= 1
            bank_config[bank_idx] += 1

        # Count redistribution
        redis_count += 1

    # Return difference between observed cycles for repeat dis
    return redis_count - seen_bank_configs[tuple(bank_config)]


if __name__ == '__main__':
    main()
