# หาร3ลงตัว -> fizz , หาร5ลงตัว -> buzz ถ้าไม่ใช่ return ตัวเลข
# 3, 6, 9 -> fizz
# 5, 10, 20 -> buzz
# 15, 30, 45 -> fizzbuzz
# 1, 2, 4 -> number

from fizzbuzz import fizzbuzz
import unittest


class FizzbuzzTest(unittest.TestCase):
    def test_fizzbuzz_push_1_should_be_return_1(self):
        # arrange - prepare before test
        expected = "1"
        # action
        actaul = fizzbuzz(1)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_2_should_be_return_2(self):
        # arrange - prepare before test
        expected = "2"
        # action
        actaul = fizzbuzz(2)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_4_should_be_return_4(self):
        # arrange - prepare before test
        expected = "4"
        # action
        actaul = fizzbuzz(4)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_3_should_be_return_fizz(self):
        # arrange - prepare before test
        expected = "fizz"
        # action
        actaul = fizzbuzz(3)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_6_should_be_return_fizz(self):
        # arrange - prepare before test
        expected = "fizz"
        # action
        actaul = fizzbuzz(6)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_9_should_be_return_fizz(self):
        # arrange - prepare before test
        expected = "fizz"
        # action
        actaul = fizzbuzz(9)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_5_should_be_return_buzz(self):
        # arrange - prepare before test
        expected = "buzz"
        # action
        actaul = fizzbuzz(5)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_10_should_be_return_buzz(self):
        # arrange - prepare before test
        expected = "buzz"
        # action
        actaul = fizzbuzz(10)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_15_should_be_return_fizzbuzz(self):
        # arrange - prepare before test
        expected = "fizzbuzz"
        # action
        actaul = fizzbuzz(15)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_30_should_be_return_fizzbuzz(self):
        # arrange - prepare before test
        expected = "fizzbuzz"
        # action
        actaul = fizzbuzz(30)
        # assert
        self.assertEquals(expected, actaul)

    def test_fizzbuzz_push_45_should_be_return_fizzbuzz(self):
        # arrange - prepare before test
        expected = "fizzbuzz"
        # action
        actaul = fizzbuzz(45)
        # assert
        self.assertEquals(expected, actaul)