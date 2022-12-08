from prepare import Prepare

class GameRunning:
    def __init__(self):
        self.prepare = Prepare()

    def check_target(self, player_list):
        while True:
            print("Kirjoita oma nimesi, niin näet kohteesi")
            own_name = input("Oma nimesi: ")
            if own_name in player_list:
                player_index = player_list.index(own_name)
                if player_index == len(player_list) -1:
                    target_index = 0
                else:
                    target_index = player_index + 1
                print(f"Kohteesi on {player_list[target_index]}")
            else:
                print("Nimeä ei löydy pelaajien joukosta!")  

