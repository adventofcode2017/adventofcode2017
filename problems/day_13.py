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
        token_gen = (line.rstrip().split(': ') for line in fh)
        layers = [(int(p), int(d)) for p, d in token_gen]

    print('Part one:', part_one(layers))
    print('Part two:', part_two(layers))


def part_one(layers):
    # Return variable
    severity = 0

    # Discover captured layers, ignoring layer zero
    for layer_position, layer_depth in layers[1:]:
        layer_period = (layer_depth - 1) * 2

        # Check if the scanner will be on zero depth when we reach it
        if (layer_position % layer_period) == 0:
            severity += (layer_position * layer_depth)

    return severity


def part_two(layers):
    delay = 0
    while True:
        delay += 1
        # For each later, check if we have been captured
        for layer_position, layer_depth in layers:
            layer_period = (layer_depth - 1) * 2

            if ((layer_position + delay) % layer_period) == 0:
                # Stop iteration and increment delay
                break
        else:
            # If we are not captured, break while loop
            break

    return delay


if __name__ == '__main__':
    main()
