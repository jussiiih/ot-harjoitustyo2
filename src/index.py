from prepare import Prepare

class SecrectMurderGame:
    def __init__(self):
        self.prepare = Prepare()

    def start(self):
        self.guide()
        self.prepare.input_player()


    def guide (self):
        print("Kirjoita pelaajan nimi, ja paina ENTER.")
        print("Kun kaikki pelaajat on kirjattu, kirjoita valmis")

application = SecrectMurderGame()
application.start()