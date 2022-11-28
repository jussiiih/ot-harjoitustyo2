import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

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

    #Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu,
    #kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta

    

