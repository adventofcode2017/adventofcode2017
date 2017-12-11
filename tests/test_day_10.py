#!/usr/bin/env python3
import unittest


from problems import day_10


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        numbers = list(range(5))
        data = '3,4,1,5'
        self.assertEqual(day_10.part_one(data, numbers), 12)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        data = ''
        data_hash = 'a2582a3a0e66e6e86e3812dcb672a272'
        self.assertEqual(day_10.part_two(data), data_hash)


    def test_two(self):
        data = 'AoC 2017'
        data_hash = '33efeb34ea91902bb2f59c9920caa6cd'
        self.assertEqual(day_10.part_two(data), data_hash)


    def test_three(self):
        data = '1,2,3'
        data_hash = '3efbe78a8d82f29979031a4aa0b16a9d'
        self.assertEqual(day_10.part_two(data), data_hash)


    def test_four(self):
        data = '1,2,4'
        data_hash = '63960835bcdc130f0b66d7ff4f6a5a8e'
        self.assertEqual(day_10.part_two(data), data_hash)
