#!/usr/bin/env python3
import unittest

from problems import day_03


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        self.assertEqual(day_03.part_one(1), 0)

    def test_two(self):
        self.assertEqual(day_03.part_one(12), 3)

    def test_three(self):
        self.assertEqual(day_03.part_one(23), 2)

    def test_four(self):
        self.assertEqual(day_03.part_one(1024), 31)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        self.assertEqual(day_03.part_two(10), 11)

    def test_two(self):
        self.assertEqual(day_03.part_two(133), 142)

    def test_three(self):
        self.assertEqual(day_03.part_two(330), 351)

    def test_four(self):
        self.assertEqual(day_03.part_two(747), 806)
