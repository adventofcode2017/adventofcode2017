#!/usr/bin/env python3
import unittest


from problems import day_15


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        gen_a = 65
        gen_b = 8921
        self.assertEqual(day_15.part_one(gen_a, gen_b, int(4e4), False), 3)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        gen_a = 65
        gen_b = 8921
        self.assertEqual(day_15.part_two(gen_a, gen_b, int(4e4), False), 4)
