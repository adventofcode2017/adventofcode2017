#!/usr/bin/env python3
import argparse
import pathlib
import re


inst_regex = re.compile(r'^([a-z]+) (dec|inc) (-?[0-9]+) if ([a-z]+) ([=!<>]+) (-?[0-9]+)$')


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
        line_re_results = (inst_regex.match(line.rstrip()) for line in fh)
        instructions = [d.groups() for d in line_re_results]

    print('Part one:', part_one(instructions))
    print('Part two:', part_two(instructions))


def get_register_value(key, registers):
    try:
        return registers[key]
    except KeyError:
        registers[key] = 0
        return 0


def execute_instruction(ins_tokens, registers):
    # Conditional check by eval'ing the entire thing ¯\_(ツ)_/¯; skip on false
    register_value = get_register_value(ins_tokens[3], registers)
    if not eval(str(register_value) + ins_tokens[4] + ins_tokens[5]):
        return

    # Ensure register exists and if not, set to zero
    if ins_tokens[0] not in registers:
        registers[ins_tokens[0]] = 0

    # Apply instruction
    if ins_tokens[1] == 'inc':
        registers[ins_tokens[0]] += int(ins_tokens[2])
    elif ins_tokens[1] == 'dec':
        registers[ins_tokens[0]] -= int(ins_tokens[2])


def part_one(instructions):
    registers = dict()

    for ins_tokens in instructions:
        execute_instruction(ins_tokens, registers)

    return max(registers.values())


def part_two(instructions):
    registers = dict()
    max_value = 0

    for ins_tokens in instructions:
        execute_instruction(ins_tokens, registers)
        if max(registers.values()) > max_value:
            max_value = max(registers.values())

    return max_value


if __name__ == '__main__':
    main()
