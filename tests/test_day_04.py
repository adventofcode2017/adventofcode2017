#!/usr/bin/env python3
import unittest


from problems import day_04


def prepare_passphrase(passphrase):
    return [passphrase.split()]


class TestExamplesPartOne(unittest.TestCase):

    def test_one(self):
        passphrase = prepare_passphrase('aa bb cc dd ee')
        self.assertEqual(day_04.part_one(passphrase), 1)


    def test_two(self):
        passphrase = prepare_passphrase('aa bb cc dd aa')
        self.assertEqual(day_04.part_one(passphrase), 0)


    def test_three(self):
        passphrase = prepare_passphrase('aa bb cc dd aaa')
        self.assertEqual(day_04.part_one(passphrase), 1)


class TestExamplesPartTwo(unittest.TestCase):

    def test_one(self):
        passphrase = prepare_passphrase('abcde fghij')
        self.assertEqual(day_04.part_two(passphrase), 1)


    def test_two(self):
        passphrase = prepare_passphrase('abcde xyz ecdab')
        self.assertEqual(day_04.part_two(passphrase), 0)


    def test_three(self):
        passphrase = prepare_passphrase('a ab abc abd abf abj')
        self.assertEqual(day_04.part_two(passphrase), 1)


    def test_four(self):
        passphrase = prepare_passphrase('iiii oiii ooii oooi oooo')
        self.assertEqual(day_04.part_two(passphrase), 1)


    def test_five(self):
        passphrase = prepare_passphrase('oiii ioii iioi iiio')
        self.assertEqual(day_04.part_two(passphrase), 0)
