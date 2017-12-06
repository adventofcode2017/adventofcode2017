#!/usr/bin/env python3
import unittest


from problems import day_06


bank_config = [0, 2, 7, 0]


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        self.assertEqual(day_06.part_one(bank_config), 5)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        self.assertEqual(day_06.part_two(bank_config), 4)
