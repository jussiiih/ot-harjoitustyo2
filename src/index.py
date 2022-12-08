from prepare import Prepare
from game_running import GameRunning

class SecrectMurderGame:
    def __init__(self):
        self.prepare = Prepare()
        self.game_running = GameRunning()

    def start(self):
        self.guide()
        self.game_running.check_target(self.prepare.input_player())

    def guide (self):
        print("Kirjoita pelaajan nimi, ja paina ENTER.")
        print("Kun kaikki pelaajat on kirjattu, kirjoita valmis")

application = SecrectMurderGame()
application.start()