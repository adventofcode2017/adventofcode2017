#!/usr/bin/env python3
import unittest


from problems import day_12


data = ('''0 <-> 2
           1 <-> 1
           2 <-> 0, 3, 4
           3 <-> 2, 4
           4 <-> 2, 3, 6
           5 <-> 6
           6 <-> 4, 5''')


def parse_pipes(data):
    line_gen = (line.strip() for line in data.split('\n'))
    group_gen = (day_12.pipe_re.match(line).groups() for line in line_gen)
    return {pin: set(pout.split(', ')) for pin, pout in group_gen}


class TestExamplesPartOne(unittest.TestCase):

    def setUp(self):
        self.pipes = parse_pipes(data)

    def test_one(self):
        self.assertEqual(day_12.part_one(self.pipes), 6)


class TestExamplesPartTwo(unittest.TestCase):

    def setUp(self):
        self.pipes = parse_pipes(data)

    def test_one(self):
        self.assertEqual(day_12.part_two(self.pipes), 2)
