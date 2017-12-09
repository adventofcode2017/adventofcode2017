#!/usr/bin/env python3
import unittest


from problems import day_08


test_input = ('''b inc 5 if a > 1
                 a inc 1 if b < 5
                 c dec -10 if a >= 1
                 c inc -20 if c == 10''')



def parse_input(test_input):
    input_lines = (line.strip() for line in test_input.split('\n'))
    line_re_results = (day_08.inst_regex.match(line.rstrip()) for line in input_lines)
    return [d.groups() for d in line_re_results]


class TestExamplesPartOne(unittest.TestCase):

    def setUp(self):
        self.instructions = parse_input(test_input)


    def test_one(self):
        self.assertEqual(day_08.part_one(self.instructions), 1)


class TestExamplesPartTwo(unittest.TestCase):

    def setUp(self):
        self.instructions = parse_input(test_input)


    def test_one(self):
        self.assertEqual(day_08.part_two(self.instructions), 10)
