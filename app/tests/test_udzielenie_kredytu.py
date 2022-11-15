import unittest
from ..Konto import Konto
from parameterized import parameterized

class TestUdzielenieKredytu(unittest.TestCase):
    
    imie = "michal"
    nazwisko = "swistowski"
    pesel = "02222222222"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([500, 300], 300, False, 0),
        ([-500, 500, 500, 300], 2000, True, 2000),
        ([-500, 500, -500, 300], 300, False, 0),
        ([700, -300, 500, -500, 1700], 2000, True, 2000),
        ([-300, -500, 400, 400, -700], 2000, False, 0)
        ])
        
    def test_kredyt(self, historia, kwota, oczekiwane_przyznanie, oczekiwane_saldo):
        self.konto.historia = historia
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota), oczekiwane_przyznanie)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)

    # def test_warunek_ponizej_3_wplat(self):
    #     self.konto.historia = [500, 300]
    #     self.assertFalse(self.konto.zaciagnij_kredyt(300))
    #     self.assertEqual(self.konto.saldo, 0)

    # def test_warunek_3_wplaty_kredyt_udane(self):
    #     self.konto.historia = [-500, 500, 500, 300]
    #     self.assertTrue(self.konto.zaciagnij_kredyt(2000))
    #     self.assertEqual(self.konto.saldo, 2000)

    # def test_warunek_3_wplaty_kredyt_nieudane(self):
    #     self.konto.historia = [-500, 500, -500, 300]
    #     self.assertFalse(self.konto.zaciagnij_kredyt(300))
    #     self.assertEqual(self.konto.saldo, 0)

    # def test_suma_5_transakcji_kredyt_udane(self):
    #     self.konto.historia = [700, -300, 500, -500, 1700]
    #     self.assertTrue(self.konto.zaciagnij_kredyt(2000))
    #     self.assertEqual(self.konto.saldo, 2000)

    # def test_suma_5_transakcji_kredyt_nieudane(self):
    #     self.konto.historia = [-300, -500, 400, 400, -700]
    #     self.assertFalse(self.konto.zaciagnij_kredyt(2000))
    #     self.assertEqual(self.konto.saldo, 0)
