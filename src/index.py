from prepare import Prepare

class GameStart:
    def __init__(self):
        self.prepare = Prepare()

    def start(self):
        self.guide()

        while True:
            player_name = input("Kirjoita pelaajan nimi")
            
            if player_name == "valmis":
                if len(self.prepare.players) < 3:
                    print('Pelaajia täytyy olla vähintään 3')
                    continue
                else:
                    self.prepare.shuffle_players
                    break

            if len(player) < 2:
                print("Nimessä täytyy olla vähintään 2 kirjainta!")
                continue
            
            forbidden_characters = ""
            
            if player_name in self.prepare.players:
                print("Nimi on jo käytössä!")
                continue

            self.prepare.add_player


    def guide (self):
        print("Kirjoita pelaajan nimi, ja paina ENTER.")
        print("Kun kaikki pelaajat on kirjattu, kirjoita valmis")
