#!/usr/bin/env python3
import unittest


from problems import day_16


class TestData(unittest.TestCase):

    def setUp(self):
        self.programs = ['a', 'b', 'c', 'd', 'e']
        self.instructions = [
                ('s', 1),
                ('x', 3, 4),
                ('p', 'e', 'b')
                ]


class TestExamplesPartOne(TestData):

    def test_one(self):
        self.assertEqual(day_16.part_one(self.programs, self.instructions), 'baedc')


class TestExamplesPartTwo(TestData):

    def test_one(self):
        programs = self.programs[:]
        iterations = 2
        for i in range(iterations):
            programs = day_16.run_iteration(programs, self.instructions)
        self.assertEqual(programs, ['c', 'e', 'a', 'd', 'b'])


    def test_two(self):
        programs = self.programs[:]
        self.assertEqual(day_16.part_two(programs, self.instructions, int(1e9)), 'abcde')
