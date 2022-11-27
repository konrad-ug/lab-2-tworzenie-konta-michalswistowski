from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe
import unittest

class TestHistory(unittest.TestCase):

    imie = "michal"
    nazwisko = "swistowski"
    pesel = "02222222222"

    nazwafirmy = "jajco.inc"
    NIP = "12345678910"

    def test_historia_przelew_wychodzacy_udany(self):
        konto = Konto(self.imie, self.nazwisko, self.nazwisko)
        konto.saldo = 600
        konto.zaksieguj_przelew_wychodzacy(500)
        self.assertEqual(konto.historia, [-500])

    def test_historia_przelew_wychodzacy_nieudany(self):
        konto = Konto(self.imie, self.nazwisko, self.nazwisko)
        konto.saldo = 400
        konto.zaksieguj_przelew_wychodzacy(500)
        self.assertEqual(konto.historia, [])
    
    def test_historia_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.nazwisko)
        konto.zaksieguj_przelew_przychodzacy(500)
        self.assertEqual(konto.historia, [500])

    def test_historia_kilka_przelewow_udane(self):
        konto = Konto(self.imie, self.nazwisko, self.nazwisko)
        konto.zaksieguj_przelew_przychodzacy(400)
        konto.zaksieguj_przelew_wychodzacy(300)
        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.historia, [400, -300, 300])

    def test_historia_kilka_przelewow_nieudane(self):
        konto = Konto(self.imie, self.nazwisko, self.nazwisko)
        konto.zaksieguj_przelew_przychodzacy(400)
        konto.zaksieguj_przelew_wychodzacy(500)
        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.historia, [400, 300])
    
    def test_historia_przelew_ekspresowy_udany(self):
        konto = Konto(self.imie, self.nazwisko, self.nazwisko)
        konto.saldo = 500
        konto.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(konto.historia, [-300, -1])

    def test_historia_przelew_ekspresowy_saldo_ujemne_pooplacie(self):
        konto = Konto(self.imie, self.nazwisko, self.nazwisko)
        konto.saldo = 500
        konto.zaksieguj_przelew_ekspresowy(500)
        self.assertEqual(konto.historia, [-500, -1])

    def test_historia_przelew_ekspresowy_nieudany(self):
        konto = Konto(self.imie, self.nazwisko, self.nazwisko)
        konto.saldo = 500
        konto.zaksieguj_przelew_ekspresowy(600)
        self.assertEqual(konto.historia, [])
    
