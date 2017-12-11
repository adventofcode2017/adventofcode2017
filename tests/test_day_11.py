#!/usr/bin/env python3
import unittest


from problems import day_11


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        instructions = ['ne', 'ne', 'ne']
        self.assertEqual(day_11.part_one(instructions), 3)


    def test_two(self):
        instructions = ['ne', 'ne', 'sw', 'sw']
        self.assertEqual(day_11.part_one(instructions), 0)


    def test_three(self):
        instructions = ['ne', 'ne', 's', 's']
        self.assertEqual(day_11.part_one(instructions), 2)


    def test_four(self):
        instructions = ['se', 'sw', 'se', 'sw', 'sw']
        self.assertEqual(day_11.part_one(instructions), 3)
