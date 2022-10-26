import unittest
import re

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "11111111111")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "11111111111", "brak peselu!")
        

    def test_inna_dlugosc_pesel(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "11111111111")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "niepoprawny pesel!")


    def test_promocja_nieprawidlowo(self):
        konto = Konto("Dariusz", "Januszewski", "11111111111", "PROM_BCDfg")
        self.assertEqual(konto.saldo, 0, "mimo nieprawidlowego kodu dodano 50zl!")

    def test_promocja_po60_przed2000(self):
        konto = Konto("Dariusz", "Januszewski", "71111111111", "PROM_BCD")
        self.assertEqual(konto.saldo, 50, "niedodano promocji!")

    def test_promocja_po60_po2000(self):
        konto = Konto("Dariusz", "Januszewski", "11301111111", "PROM_BCD")
        self.assertEqual(konto.saldo, 50, "niedodano promocji!")


    def test_promocja_przed60(self):
        konto = Konto("Dariusz", "Januszewski", "58111111111", "PROM_BCDfg")
        self.assertEqual(konto.saldo, 0, "nieslusznie dodano promocje!")