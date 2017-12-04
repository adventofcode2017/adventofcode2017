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
        passphrases = [line.rstrip().split() for line in fh]

    print('Part one:', part_one(passphrases))
    print('Part two:', part_two(passphrases))


def part_one(passphrases):
    # Return variable
    count = 0

    for passphrase in passphrases:
        # Set to captured observed words
        words = set()
        for word in passphrase:
            if word in words:
                break
            else:
                words.add(word)
        else:
            # Count only if we didn't break
            count += 1

    return count


def part_two(passphrases):
    # Return variable
    count = 0

    for passphrase in passphrases:
        # Set to captured observed words
        words = set()
        for word in passphrase:
            # Sort letters as order in anagrams do not matter
            word_sorted = ''.join(sorted(word))
            if word_sorted in words:
                break
            else:
                words.add(word_sorted)
        else:
            # Count only if we didn't break
            count += 1

    return count


if __name__ == '__main__':
    main()
