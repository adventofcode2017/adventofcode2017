#!/usr/bin/env python3
import unittest


from problems import day_07


test_input = ('''pbga (66)
                 xhth (57)
                 ebii (61)
                 havc (66)
                 ktlj (57)
                 fwft (72) -> ktlj, cntj, xhth
                 qoyq (66)
                 padx (45) -> pbga, havc, qoyq
                 tknk (41) -> ugml, padx, fwft
                 jptl (61)
                 ugml (68) -> gyxo, ebii, jptl
                 gyxo (61)
                 cntj (57)''')


def parse_input(test_input):
    input_lines = test_input.split('\n')
    token_gen = (day_07.parse_program(line.strip()) for line in input_lines)
    return {n: (w, c) for n, w, c in token_gen}


class TestExamplesPartOne(unittest.TestCase):

    def setUp(self):
        self.programs = parse_input(test_input)


    def test_one(self):
        self.assertEqual(day_07.part_one(self.programs), 'tknk')


class TestExamplesPartTwo(unittest.TestCase):

    def setUp(self):
        self.programs = parse_input(test_input)


    def test_one(self):
        self.assertEqual(day_07.part_two(self.programs), 60)
