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

    def test_edulliseen_tarpeeksi_rahaa_summa_kortilta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukkaaseen_tarpeeksi_rahaa_summa_kortilta(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_edulliseen_tarpeeksi_rahaa_lounasmaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaaseen_tarpeeksi_rahaa_lounasmaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edulliseen_ei_tarpeeksi_rahaa_saldo_pysyy(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_maukkaseen_ei_tarpeeksi_rahaa_saldo_pysyy(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 300)

    def test_edulliseen_ei_tarpeeksi_rahaa_saldo_pysyy(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaaseen_ei_tarpeeksi_rahaa_saldo_pysyy(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliseen_ei_tarpeeksi_saldoa_palauta_false(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_maukkaaseen_ei_tarpeeksi_saldoa_palauta_false(self):
        kortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_edulliseen_ei_tarpeeksi_saldoa_kassa_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaaseen_ei_tarpeeksi_saldoa_kassa_ei_muutu(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_latauksessa_kortin_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_latauksessa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

####

    def test_kateinen_ei_riita_edulliseen_kassa_pysyy(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateinen_ei_riita_edulliseen_lounasmaara_pysyy(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateinen_ei_riita_maukkaaseen_kassa_pysyy(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateinen_ei_riita_maukkaaseen_lounasmaara_pysyy(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortin_lataus_negatiivinen_kassa_pysyy(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataus_negatiivinen_kortin_saldo_pysyy(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)

    
