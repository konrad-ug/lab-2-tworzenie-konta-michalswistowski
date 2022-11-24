import unittest
from app.Konto import Konto
from app.RejestrKont import RejestrKont

class TestRejestrKont(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.konto_pierwsze = Konto("michal", "swistowski", "12345678901")
        cls.konto_drugie = Konto("kacper", "jaworowski", "42345678901")
        cls.konto_trzecie = Konto("dominik", "rutkowski", "09876543211")

    def test_1_dodaj_konto(cls):
        RejestrKont.dodaj(cls.konto_pierwsze)
        cls.assertEqual(RejestrKont.iloscKont(), 1)

    def test_2_dodaj_kolejne_konto(cls):
        RejestrKont.dodaj(cls.konto_drugie)
        cls.assertEqual(RejestrKont.iloscKont(), 2)
        
    def test_3_wyszukaj_rejestr(cls):
        RejestrKont.dodaj(cls.konto_trzecie)
        cls.assertEqual(RejestrKont.szukaj("09876543211"), cls.konto_trzecie)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []