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
        instruction_gen = (ins for ins in fh.read().rstrip().split(','))
        instructions = [parse_instructions(ins) for ins in instruction_gen]

    # Get programs list; a->p
    programs = [chr(n) for n in range(97, 113)]

    print('Part one:', part_one(programs[:], instructions))
    print('Part two:', part_two(programs[:], instructions, int(1e9)))


def parse_instructions(instruction):
    if instruction.startswith('s'):
        return ('s', int(instruction[1:]))
    elif instruction.startswith('x'):
        return ('x', *[int(d) for d in instruction[1:].split('/')])
    elif instruction.startswith('p'):
        return ('p', *instruction[1:].split('/'))


def run_iteration(programs, instructions):
    # Using std list rather than linked
    for instruction in instructions:
        op, *args = instruction
        if op == 's':
            dist = args[0]
            programs = programs[-dist:] + programs[:-dist]
        elif op == 'x':
            i, j = args
            tmp = programs[i]
            programs[i] = programs[j]
            programs[j] = tmp
        elif op == 'p':
            a, b = args
            i = programs.index(a)
            j = programs.index(b)
            tmp = programs[i]
            programs[i] = programs[j]
            programs[j] = tmp

    return programs


def part_one(programs, instructions):
    return ''.join(run_iteration(programs, instructions))


def part_two(programs, instructions, diter=2):
    seen = set()
    cycle_order = list()

    for i in range(diter):
        # Check if we have cycled through
        if tuple(programs) in seen:
            break

        seen.add(tuple(programs))
        cycle_order.append(''.join(programs))
        programs = run_iteration(programs, instructions)


    # Find position within the cycle where our iteration ends
    position = diter % len(seen)
    return ''.join(cycle_order[position])


if __name__ == '__main__':
    main()
