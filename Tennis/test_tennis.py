import unittest
from tennis import Player

class TestTennis(unittest.TestCase):
    def test_player_get_score_0_0(self):
        expected = "0 - 0"
        a = Player("A")
        b = Player("B")
        self.assertEquals(expected, f"{a.get_score()} - {b.get_score()}")

    def test_add_point_player_get_score_15_0(self):
        expected = "15 - 0"
        a = Player("A")
        b = Player("B")
        a.add_point()
        self.assertEquals(expected, f"{a.get_score()} - {b.get_score()}")

    def test_add_point_player_get_score_15_15(self):
        expected = "15 - 15"
        a = Player("A")
        b = Player("B")
        a.add_point()
        b.add_point()
        self.assertEquals(expected, f"{a.get_score()} - {b.get_score()}")

    def test_add_point_player_get_score_30_15(self):
        expected = "30 - 15"
        a = Player("A")
        b = Player("B")
        a.add_point()
        a.add_point()
        b.add_point()
        self.assertEquals(expected, f"{a.get_score()} - {b.get_score()}")