#!/usr/bin/env python3
import unittest


from problems import day_14


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        hash_input = 'flqrgnkx'
        self.assertEqual(day_14.part_one(hash_input), 8108)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        hash_input = 'flqrgnkx'
        self.assertEqual(day_14.part_two(hash_input), 1242)
