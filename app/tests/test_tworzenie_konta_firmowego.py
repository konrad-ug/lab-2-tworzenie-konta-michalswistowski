
import unittest

from ..KontoFirmowe import KontoFirmowe

class testTworzenieKontaFirmowego(unittest.TestCase):

    def test_tworzenie_konta(self):
        kontofirmowe = KontoFirmowe("jajco.inc", "1234567891")
        self.assertEqual(kontofirmowe.NazwaFirmy, "jajco.inc", "Nazwa firmy nie została zapisana!")
        self.assertEqual(kontofirmowe.NIP, "1234567891", "NIP nie został napisany!")
    
    def test_Niepoprawny_NIP(self):
        kontofirmowe = KontoFirmowe("jajco.inc", "12345678910")
        self.assertEqual(kontofirmowe.NIP, "Niepoprawny NIP!")
