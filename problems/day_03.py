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
        value = int(fh.read().rstrip())

    print('Part one:', part_one(value))
    print('Part two:', part_two(value))


def part_one(cell):
    # Catch for initial origin
    if cell == 1:
        return 0

    # Quickly jump to origin of shell containing cell
    cell_count = 1
    shell = 1
    while True:
        # Check if we fall into current shell
        if cell <= (cell_count + 8 * shell):
            break

        # If not, increment
        cell_count += 8 * shell
        shell += 1

    # Set start position of shell
    x = shell
    y = -(shell - 1)

    # Jump to exact location
    cell_dist = cell - cell_count
    shell_edge = shell * 2
    cell_location = cell_dist // shell_edge

    if cell_location == 0:
        # Apply +y
        y += cell_dist - 1
    elif cell_location == 1:
        # Apply max +y and -x
        y += shell_edge - 1
        x -= (cell_dist % shell_edge)
    elif cell_location == 2:
        # Apply -y and max -x
        y = (y + shell_edge - 1) - (cell_dist % shell_edge)
        x -= shell_edge
    elif cell_location == 3:
        # Apply max -y and +x
        y -= 1
        x -= (cell_dist % shell_edge)
    elif cell_location == 4:
        # Apply max -y
        y -= 1

    # Return Manhattan distance
    return abs(x) + abs(y)


def part_two(input_value):
    # Init values list with origin
    values = {(0, 0): 1}

    # Generator for spiral x, y position trace
    def position_gen():
        shell = 2
        position = [1, 0]

        directions = [(1, 1, 0), (0, -1, 1), (1, -1, 1), (0, 1, 1)]

        while True:
            # Set up distances
            shell_edge = (shell - 1) * 2
            distances = (shell_edge - 1, shell_edge)

            # Yield each position
            yield tuple(position)
            for coord, direction, distance in directions:
                for i in range(distances[distance]):
                    position[coord] += direction
                    yield tuple(position)

            # Bump to next shell origin
            position[0] += 1
            shell += 1


    # Collect all neighbours of position
    def get_neighbours(position):
        opts = (1, 0, -1)
        for i in opts:
            for j in opts:
                if (i, j) == (0, 0):
                    continue
                yield (position[0] + i, position[1] + j)


    # Look up neighbour values
    def neighbour_value(position):
        try:
            return values[position]
        except KeyError:
            return 0


    # Walk through cells
    for i, position in enumerate(position_gen(), 2):
        # TODO: be more considerate with neighbour selection, current inefficient
        # Get all neighbours, check bounds at list index lookup
        value = sum((neighbour_value(n) for n in get_neighbours(position)))

        # Return if we reach the answer
        if value > input_value:
            return value

        # Add value to hash
        values[position] = value


if __name__ == '__main__':
    main()
