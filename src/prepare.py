import random

class Prepare:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        self.players.append(name)

    def shuffle_players(self):
        random.shuffle(self.players)

    def input_player(self):
        while True:
            player_name = input("Kirjoita pelaajan nimi: ")

            if player_name == "valmis":
                if len(self.players) < 3:
                    print('Pelaajia täytyy olla vähintään 3')
                    continue
                else:
                    self.shuffle_players()
                    break
            
            if len(player_name) < 2:
                print('Nimessä täytyy olla vähintään 2 kirjainta!')
                continue
            
            forbidden_charactes = "§1234567890!+´½!#¤%&/()=?`@£${[]}\¨'^*~<>|/-,.-;:_"
            if any(character in forbidden_charactes for character in player_name):
                print('Nimessä saa olla vain kirjaimia ja välilyöntejä!')

            if player_name in self.players:
                print("Nimi on jo käytössä!")
                continue

            self.add_player(player_name)   
