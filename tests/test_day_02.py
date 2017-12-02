#!/usr/bin/env python3
import unittest

from problems import day_02


class TestExamplesPartOne(unittest.TestCase):

    def setUp(self):
        self.rows = [[5, 1, 9, 5],
                     [7, 5, 3],
                     [2, 4, 6, 8]]


    def test_one(self):
        row = [self.rows[0]]
        self.assertEqual(day_02.part_one(row), 8)


    def test_two(self):
        row = [self.rows[1]]
        self.assertEqual(day_02.part_one(row), 4)


    def test_three(self):
        row = [self.rows[2]]
        self.assertEqual(day_02.part_one(row), 6)


    def test_four(self):
        self.assertEqual(day_02.part_one(self.rows), 18)


class TestExamplesPartTwo(unittest.TestCase):

    def setUp(self):
        self.rows = [[5, 9, 2, 8],
                     [9, 4, 7, 3],
                     [3, 8, 6, 5]]


    def test_one(self):
        row = [self.rows[0]]
        self.assertEqual(day_02.part_two(row), 4)


    def test_two(self):
        row = [self.rows[1]]
        self.assertEqual(day_02.part_two(row), 3)


    def test_three(self):
        row = [self.rows[2]]
        self.assertEqual(day_02.part_two(row), 2)


    def test_four(self):
        self.assertEqual(day_02.part_two(self.rows), 9)
