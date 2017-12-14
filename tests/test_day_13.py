#!/usr/bin/env python3
import unittest


from problems import day_13


data = ('''0: 3
           1: 2
           4: 4
           6: 4''')


def parse_data(data):
    line_gen = (line.strip() for line in data.split('\n'))
    token_gen = (line.rstrip().split(': ') for line in line_gen)
    return [(int(p), int(d)) for p, d in token_gen]


class TestExamplesPartOne(unittest.TestCase):

    def setUp(self):
        self.layers = parse_data(data)

    def test_one(self):
        self.assertEqual(day_13.part_one(self.layers), 24)


class TestExamplesPartTwo(unittest.TestCase):

    def setUp(self):
        self.layers = parse_data(data)

    def test_one(self):
        self.assertEqual(day_13.part_two(self.layers), 10)
