#!/usr/bin/env python3
import argparse
import pathlib
import re


program_regex = re.compile(r'^([a-z]+) \(([0-9]+)\)(?: -> )?(.+)?$')


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
        token_gen = (parse_program(ps.rstrip()) for ps in fh)
        programs = {n: (w, c) for n, w, c in token_gen}

    print('Part one:', part_one(programs))
    print('Part two:', part_two(programs))


def parse_program(program_string):
    name, weight, children = program_regex.match(program_string).groups()
    try:
        children = children.split(', ')
    except AttributeError:
        pass
    return (name, int(weight), children)


def part_one(programs):
    return get_root(programs)


def get_root(programs):
    all_children = set()
    names = set()
    for name, (weight, program_children) in programs.items():
        names.add(name)
        if program_children:
            all_children.update(program_children)

    return list(names.difference(all_children))[0]


def part_two(programs):
    weights = dict()
    root = get_root(programs)


    # Get weights across each program
    def sum_children_weight(node):
        weight, children = programs[node]

        # Call weight sum recursivly down through children
        if children:
            for child in children:
                weight += sum_children_weight(child)

        weights[node] = weight
        return weight

    sum_children_weight(root)


    # Find unbalanced program wrt to siblings
    node_stack = [root]
    while node_stack:
        # Get children of current node
        node = node_stack.pop()
        weight, nodes = programs[node]

        if not nodes:
            continue

        # Check weights
        node_weights = [weights[n] for n in nodes]
        if len(set(node_weights)) == 2:
            # Record imbalance but continue until source is discovered
            unbalanced_nodes = nodes
            unbalanced_weights = node_weights

        node_stack.extend(nodes)

    # Balance the program
    nw = dict()
    for node, weight in zip(unbalanced_nodes, unbalanced_weights):
        try:
            nw[weight].append(node)
        except KeyError:
            nw[weight] = [node]

    (t_node_w, t_node_l), (b_node_w, b_node_l) = sorted(nw.items(), key=lambda k: len(k[1]))
    imbalance = b_node_w - t_node_w
    return programs[t_node_l[0]][0] + imbalance


if __name__ == '__main__':
    main()
