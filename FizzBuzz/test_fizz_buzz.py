from random import random
import unittest
from fizzbuzz import call_fizzbuzz, fizzbuzz
from unittest.mock import MagicMock, patch


class FizzBuzzTest(unittest.TestCase):
    def test_push_1_should_be_return_1(self):
        expected = "1"
        actual = fizzbuzz(num=1)
        self.assertEquals(expected, actual)

    def test_push_2_should_be_return_2(self):
        expected = "2"
        actual = fizzbuzz(num=2)
        self.assertEquals(expected, actual)

    def test_push_3_should_be_return_fizz(self):
        expected = "fizz"
        actual = fizzbuzz(num=3)
        self.assertEquals(expected, actual)

    def test_push_4_should_be_return_4(self):
        expected = "4"
        actual = fizzbuzz(num=4)
        self.assertEquals(expected, actual)

    def test_push_5_should_be_return_buzz(self):
        expected = "buzz"
        actual = fizzbuzz(num=5)
        self.assertEquals(expected, actual)

    def test_push_6_should_be_return_fizz(self):
        expected = "fizz"
        actual = fizzbuzz(num=6)
        self.assertEquals(expected, actual)

    def test_push_7_should_be_return_7(self):
        expected = "7"
        actual = fizzbuzz(num=7)
        self.assertEquals(expected, actual)

    def test_push_9_should_be_return_fizz(self):
        expected = "fizz"
        actual = fizzbuzz(num=9)
        self.assertEquals(expected, actual)

    def test_push_10_should_be_return_buzz(self):
        expected = "buzz"
        actual = fizzbuzz(num=10)
        self.assertEquals(expected, actual)

    def test_push_15_should_be_return_fizzbuzz(self):
        expected = "fizzbuzz"
        actual = fizzbuzz(num=15)
        self.assertEquals(expected, actual)

    def test_push_30_should_be_return_fizzbuzz(self):
        expected = "fizzbuzz"
        actual = fizzbuzz(num=30)
        self.assertEquals(expected, actual)

    def test_push_45_should_be_return_fizzbuzz(self):
        expected = "fizzbuzz"
        actual = fizzbuzz(num=45)
        self.assertEquals(expected, actual)

    @patch("random.random")
    def test_random_number_1_should_be_return_1(self, mock_random):
        expected = (1, "1")
        mock_random.random.return_value = 0.01
        actual = call_fizzbuzz()
        self.assertEquals(expected, actual)