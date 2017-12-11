#!/usr/bin/env python3
import unittest


from problems import day_09


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        stream = '{}'
        self.assertEqual(day_09.part_one(stream), 1)


    def test_two(self):
        stream = '{{{}}}'
        self.assertEqual(day_09.part_one(stream), 6)


    def test_three(self):
        stream = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
        self.assertEqual(day_09.part_one(stream), 9)


    def test_four(self):
        stream = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
        self.assertEqual(day_09.part_one(stream), 9)


    def test_five(self):
        stream = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
        self.assertEqual(day_09.part_one(stream), 3)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        stream = '<>'
        self.assertEqual(day_09.part_two(stream), 0)


    def test_two(self):
        stream = '<<<<>'
        self.assertEqual(day_09.part_two(stream), 3)


    def test_three(self):
        stream = '<!!!>>'
        self.assertEqual(day_09.part_two(stream), 0)


    def test_four(self):
        stream = '<{o"i!a,<{i<a>'
        self.assertEqual(day_09.part_two(stream), 10)
