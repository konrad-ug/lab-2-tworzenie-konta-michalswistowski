import unittest
from ..Konto import Konto

class TestUdzielenieKredytu(unittest.TestCase):
    
    imie = "michal"
    nazwisko = "swistowski"
    pesel = "02222222222"

    def test_warunek_ponizej_3_wplat(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [500, 300]
        self.assertFalse(konto.zaciagnij_kredyt(300))
        self.assertEqual(konto.saldo, 0)

    def test_warunek_3_wplaty_kredyt_udane(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-500, 500, 500, 300]
        self.assertTrue(konto.zaciagnij_kredyt(2000))
        self.assertEqual(konto.saldo, 2000)

    def test_warunek_3_wplaty_kredyt_nieudane(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-500, 500, -500, 300]
        self.assertFalse(konto.zaciagnij_kredyt(300))
        self.assertEqual(konto.saldo, 0)

    def test_suma_5_transakcji_kredyt_udane(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [700, -300, 500, -500, 1700]
        self.assertTrue(konto.zaciagnij_kredyt(2000))
        self.assertEqual(konto.saldo, 2000)

    def test_suma_5_transakcji_kredyt_nieudane(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-300, -500, 400, 400, -700]
        self.assertFalse(konto.zaciagnij_kredyt(2000))
        self.assertEqual(konto.saldo, 0)
