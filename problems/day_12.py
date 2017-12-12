#!/usr/bin/env python3
import argparse
import re
import pathlib


pipe_re = re.compile(r'^([0-9]+) <-> (.+)$')


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
        group_gen = (pipe_re.match(line).groups() for line in fh)
        pipes = {pin: set(pout.split(', ')) for pin, pout in group_gen}

    print('Part one:', part_one(pipes.copy()))
    print('Part two:', part_two(pipes.copy()))


def collect_group(pipes, program):
    stack = [program]
    seen = set(stack)
    while stack:
        # Collect unseen programs connected to source and add to stack
        source = stack.pop()
        targets = pipes.pop(source)
        targets_unseen = [t for t in targets if t not in seen]
        stack.extend(targets_unseen)

        # Record programs seen in this group
        seen.update(targets_unseen)

    return seen


def part_one(pipes):
    group = collect_group(pipes, '0')
    return len(group)


def part_two(pipes):
    groups = 0
    while pipes:
        # Get the next key and seed grouping method
        program = list(pipes)[0]
        collect_group(pipes, program)

        # Count group
        groups += 1

    return groups


if __name__ == '__main__':
    main()
