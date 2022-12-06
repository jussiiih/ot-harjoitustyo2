from prepare import Prepare

class GameRunning:
    def __init__(self):
        self.shuffled_players = prepare.self.players

    def check_target():
        while True:
            print("Kirjoita oma nimesi, niin näet kohteesi")
            own_name = input("Oma nimesi: ")
            if own_name in self.shuffled_players:
                player_index = self.shuffled_players.index(own_name)
                if player_index == len(self.shuffled_players - 1):
                    target_index = 0
                else:
                    target_index = player_index + 1
                print(f"Kohteesi on {self.shuffled_players[target_index]}")

