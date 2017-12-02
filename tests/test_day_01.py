#!/usr/bin/env python3
import unittest


from problems import day_01


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        digits = [1, 1, 2, 2]
        self.assertEqual(day_01.part_one(digits), 3)


    def test_two(self):
        digits = [1, 1, 1, 1]
        self.assertEqual(day_01.part_one(digits), 4)


    def test_three(self):
        digits = [1, 2, 3, 4]
        self.assertEqual(day_01.part_one(digits), 0)


    def test_four(self):
        digits = [9, 1, 2, 1, 2, 1, 2, 9]
        self.assertEqual(day_01.part_one(digits), 9)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        digits = [1, 2, 1, 2]
        self.assertEqual(day_01.part_two(digits), 6)


    def test_two(self):
        digits = [1, 2, 2, 1]
        self.assertEqual(day_01.part_two(digits), 0)


    def test_three(self):
        digits = [1, 2, 3, 4, 2, 5]
        self.assertEqual(day_01.part_two(digits), 4)


    def test_four(self):
        digits = [1, 2, 3, 1, 2, 3]
        self.assertEqual(day_01.part_two(digits), 12)


    def test_five(self):
        digits = [1, 2, 1, 3, 1, 4, 1, 5]
        self.assertEqual(day_01.part_two(digits), 4)
