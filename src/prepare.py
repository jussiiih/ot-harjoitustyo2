import random

class Prepare:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        self.players.append(name)

    def shuffle_players(self):
        random.shuffle(self.players)