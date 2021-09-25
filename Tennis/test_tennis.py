import unittest
from tennis import Player

class TestTennis(unittest.TestCase):
    def test_player_get_score_0_0(self):
        expected = "0 - 0"
        a = Player("A")
        b = Player("B")
        a_score = a.get_score()
        b_score = b.get_score()
        self.assertEquals(expected, f"{a_score} - {b_score}")

    def test_add_point_player_get_score_15_0(self):
        expected = "15 - 0"
        a = Player("A")
        b = Player("B")
        a_point = a.add_point()
        self.assertEquals(expected, f"{a_point} - {b.point}")