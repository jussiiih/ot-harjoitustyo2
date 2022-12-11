import unittest
from prepare import Prepare


class TestPrepare(unittest.TestCase):
    def setUp(self):
        self.prepare = Prepare()

    def test_at_first_player_list_is_empty(self):
        self.assertEqual(self.prepare.players, [])

    def test_add_players(self):
        self.prepare.add_player("Matti")
        self.prepare.add_player("Maija")
        self.assertEqual(self.prepare.players, ["Matti", "Maija"])

    def test_player_name_must_be_over_one_character(self):
        self.prepare.add_player("M")
        self.assertEqual(self.prepare.players, [])

    def test_player_name_cannot_have_forbidden_character(self):
        self.prepare.add_player("Matti3")
        self.assertEqual(self.prepare.players, [])

    def test_player_names_cannot_be_same(self):
        self.prepare.add_player("Matti")
        self.prepare.add_player("Matti")
        self.assertEqual(self.prepare.players, ["Matti"])
    