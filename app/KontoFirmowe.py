from app.Konto import Konto

class KontoFirmowe(Konto):

    def __init__(self, NazwaFirmy, NIP):
        self.NazwaFirmy = NazwaFirmy
        self.NIP = NIP
        self.saldo = 0
        self.niepoprawny_NIP(NIP)
        self.konto_biznesowe = True
    
    def niepoprawny_NIP(self, NIP):
        if (len(NIP) != 10):
            self.NIP = "Niepoprawny NIP!"
        else:
            self.NIP = NIP

