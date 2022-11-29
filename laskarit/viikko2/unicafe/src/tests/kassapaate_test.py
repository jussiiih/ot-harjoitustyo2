import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_alussa_kassassa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_kassassa_edullisia_myyty_oikea_maara(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_alussa_maukkaita_myyty_oikea_maara(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_oikea_vaihtoraha_edullisesta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_kassa_oikein_edullisen_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_edullisten_maara_kasvaa_kateisostolla(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_oikea_vaihtoraha_maukkaasta(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kassa_oikein_maukkaan_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaiden_maara_kasvaa_kateisostolla(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def edullisen_maksu_ei_riita_kassassa_raha_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def edullisen_maksu_ei_riita_maksu_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def edullisen_maksu_ei_riita_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def maukkaan_maksu_ei_riita_kassassa_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def maukkaan_maksu_ei_riita_maksu_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def maukkaan_maksu_ei_riita_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

 #seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan oikein
#Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta

 #   Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
  #  Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
   # Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
    #Kassassa oleva rahamäärä ei muutu kortilla ostettaessa

#Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    

