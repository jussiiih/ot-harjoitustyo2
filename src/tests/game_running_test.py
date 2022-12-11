import unittest
from prepare import Prepare
from game_running import GameRunning


class TestPrepare(unittest.TestCase):
    def setUp(self):
        self.prepare = Prepare()
        self.game_running = GameRunning()

    