from prepare import Prepare

class GameStart:
    def __init__(self):
        self.prepare = Prepare()

    def start(self):
        self.guide()
        self.input_player()
        self.prepare.shuffle_players()


    def input_player(self):
        while True:
            player_name = input("Kirjoita pelaajan nimi: ")

            if player_name == "valmis":
                if len(self.prepare.players) < 3:
                    print('Pelaajia täytyy olla vähintään 3')
                    continue
                else:
                    break
            
            if len(player_name) < 2:
                print('Nimessä täytyy olla vähintään 2 kirjainta!')
                continue
            
            forbidden_charactes = "§1234567890!+´½!#¤%&/()=?`@£${[]}\¨'^*~<>|/-,.-;:_"
            if any(character in forbidden_charactes for character in player_name):
                print('Nimessä saa olla vain kirjaimia ja välilyöntejä!')

            if player_name in self.prepare.players:
                print("Nimi on jo käytössä!")
                continue

            self.prepare.add_player


    def guide (self):
        print("Kirjoita pelaajan nimi, ja paina ENTER.")
        print("Kun kaikki pelaajat on kirjattu, kirjoita valmis")

application = GameStart()
application.start()