import unittest

from ..Konto import Konto


class TestPrzelewy(unittest.TestCase):

    imie="michal"
    nazwisko="swistowski"
    pesel="022222222222"

    def test_przelew_wychodzacy_udany(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(300)
        self.assertEqual(konto.saldo, 500 - 300)

    def test_przelew_wychodzacy_nieudany(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(600)
        self.assertEqual(konto.saldo, 500)
    
    def test_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.saldo, 300)

