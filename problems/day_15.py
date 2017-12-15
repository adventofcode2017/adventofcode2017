#!/usr/bin/env python3
import argparse
import pathlib
import re
import sys


init_number_re = re.compile(r'^.+?([0-9]+)$')


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
        re_results = (init_number_re.match(line.strip()) for line in fh)
        gen_a, gen_b = [int(mo.group(1)) for mo in re_results]

    print('Part one:', part_one(gen_a, gen_b))
    print('Part two:', part_two(gen_a, gen_b))


def generate_value(gen, factor, denom):
    return (gen * factor) % denom


def generate_value_modulo(gen, factor, mod, denom):
    gen = generate_value(gen, factor, denom)
    while (gen % mod) != 0:
        gen = generate_value(gen, factor, denom)
    return gen


def part_one(gen_a, gen_b, rounds=int(40e6), status=True):
    # Init variables
    factor_a = 16807
    factor_b = 48271

    denom = 2147483647

    # There must be a more efficient way to calculate this
    percent_step = 1
    count_step = int(rounds * (percent_step / 100))
    count = 0
    for n in range(rounds):
        # Print progress
        if (n % count_step) == 0 and status:
            print(format(100 * n / rounds, '3.0f'), '%', sep='', file=sys.stderr)

        # Generate next number in series
        gen_a = generate_value(gen_a, factor_a, denom)
        gen_b = generate_value(gen_b, factor_b, denom)

        # Check equality of lowest 16 bits
        if format(gen_a, '032b')[16:] == format(gen_b, '032b')[16:]:
            count += 1

    return count


def part_two(gen_a, gen_b, rounds=int(5e6), status=True):
    # Init variables
    factor_b = 48271
    mod_a = 4

    factor_a = 16807
    mod_b = 8

    denom = 2147483647

    # There must be a more efficient way to calculate this
    percent_step = 1
    count_step = int(rounds * (percent_step / 100))
    count = 0
    for n in range(rounds):
        # Print progress
        if (n % count_step) == 0 and status:
            print(format(100 * n / rounds, '3.0f'), '%', sep='', file=sys.stderr)

        # Generate next number in series
        gen_a = generate_value_modulo(gen_a, factor_a, mod_a, denom)
        gen_b = generate_value_modulo(gen_b, factor_b, mod_b, denom)

        # Check equality of lowest 16 bits
        if format(gen_a, '032b')[16:] == format(gen_b, '032b')[16:]:
            count += 1

    return count


if __name__ == '__main__':
    main()
