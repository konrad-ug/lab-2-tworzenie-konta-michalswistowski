import unittest
from app.Konto import Konto
from app.RejestrKont import RejestrKont

class TestRejestrKont(unittest.TestCase):
    
    imie = "Michal"
    nazwisko = "Swistowski"
    pesel = "12345678901"

    def test_1_dodaj_konto(self):
        konto_pierwsze = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj(konto_pierwsze)
        self.assertEqual(RejestrKont.iloscKont(), 1)

    def test_2_dodaj_kolejne_konto(self):
        konto_drugie = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj(konto_drugie)
        self.assertEqual(RejestrKont.iloscKont(), 2)

    def test_3_wyszukaj_rejestr(self):
        konto_trzecie = Konto(self.imie, self.nazwisko, "09876543211")
        RejestrKont.dodaj(konto_trzecie)
        self.assertEqual(RejestrKont.szukaj("09876543211"), konto_trzecie)