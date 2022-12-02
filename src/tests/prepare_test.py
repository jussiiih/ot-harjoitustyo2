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