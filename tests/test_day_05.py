#!/usr/bin/env python3
import unittest


from problems import day_05


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        instructions = [0, 3, 0, 1, -3]
        self.assertEqual(day_05.part_one(instructions), 5)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        instructions = [0, 3, 0, 1, -3]
        self.assertEqual(day_05.part_two(instructions), 10)
