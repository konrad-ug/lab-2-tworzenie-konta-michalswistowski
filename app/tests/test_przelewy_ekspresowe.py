import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestPrzelewyEkspresowe(unittest.TestCase):

    imie = "michal"
    nazwisko = "swistowski"
    pesel = "02222222222"

    nazwafirmy = "jajco.inc"
    NIP = "12345678910"

    def test_przelew_ekspresowy_wychodzacy_prywatny(self):
        kontoPrywatne = Konto(self.imie, self.nazwisko, self.pesel)
        kontoPrywatne.saldo = 500
        
        kontoPrywatne.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(kontoPrywatne.saldo, 500 - 300 - 1)
    
    def test_przelew_ekspresowy_wychodzacy_biznesowy(self):
        kontoFirmowe = KontoFirmowe(self.nazwafirmy, self.NIP)
        kontoFirmowe.saldo = 500

        kontoFirmowe.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(kontoFirmowe.saldo, 500 - 300 - 5)

    def test_przelew_ekspresowy_wychodzacy_prywatny_saldo_ujemne_po_oplacie(self):
        kontoPrywatne = Konto(self.imie, self.nazwisko, self.pesel)
        kontoPrywatne.saldo = 200
        
        kontoPrywatne.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(kontoPrywatne.saldo, 200 - 200 - 1)
    
    def test_przelew_ekspresowy_wychodzacy_biznesowy_saldo_ujemne_po_oplacie(self):
        kontoFirmowe = KontoFirmowe(self.nazwafirmy, self.NIP)
        kontoFirmowe.saldo = 200

        kontoFirmowe.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(kontoFirmowe.saldo, 200 - 200 - 5)

    def test_przelew_ekspresowy_wychodzacy_prywatny_saldo_ujemne_warunek(self):
        kontoPrywatne = Konto(self.imie, self.nazwisko, self.pesel)
        kontoPrywatne.saldo = 200
        
        kontoPrywatne.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(kontoPrywatne.saldo, 200)
    
    def test_przelew_ekspresowy_wychodzacy_biznesowy_saldo_ujemne_warunek(self):
        kontoFirmowe = KontoFirmowe(self.nazwafirmy, self.NIP)
        kontoFirmowe.saldo = 200

        kontoFirmowe.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(kontoFirmowe.saldo, 200)
