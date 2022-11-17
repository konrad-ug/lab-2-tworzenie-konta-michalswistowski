from parameterized import parameterized
import unittest
from ..KontoFirmowe import KontoFirmowe

class TestUdzielenieKredytuFirma(unittest.TestCase):

    nazwaFirmy = "jajco.inc"
    nipFirmy = "1234567890"

    def setUp(self):
        self.kontoFirmowe = KontoFirmowe(self.nazwaFirmy, self.nipFirmy)

    @parameterized.expand([
        ([300, 300, 1775], 700, 300, True, 1000),
        ([300, 300, 300], 900, 400, False, 900),
        ([300, 1775], 300, 400, False, 300),
        ([300, 300], 600, 700, False, 600)
    ])

    def test_kredyt_firma(self, historia, saldo, kwota, oczekiwane_przyznanie, oczekiwane_saldo):
        self.kontoFirmowe.historia = historia
        self.kontoFirmowe.saldo = saldo
        self.assertEqual(self.kontoFirmowe.zaciagnij_kredyt_firma(kwota), oczekiwane_przyznanie)
        self.assertEqual(self.kontoFirmowe.saldo, oczekiwane_saldo)