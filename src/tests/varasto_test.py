import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_liian_pieni_tilavuus_nollataan(self):
        self.varasto = Varasto(-8)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
    
    def test_laitetaan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_liikaa_laittaminen_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(18)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otetaan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(2)
        self.varasto.ota_varastosta(-7)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_liikaa_ottaminen_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(3)
        self.varasto.ota_varastosta(9)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_stringi_toimii_oikein(self):
        tmp = f"{self.varasto}"
        self.assertEqual(tmp, "saldo = 0, vielä tilaa 10")