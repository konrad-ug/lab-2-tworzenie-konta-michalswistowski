from app.Konto import Konto

class KontoFirmowe(Konto):

    def __init__(self, NazwaFirmy, NIP):
        self.NazwaFirmy = NazwaFirmy
        self.NIP = NIP
        self.saldo = 0
        self.niepoprawny_NIP(NIP)
        self.konto_biznesowe = True
        self.historia = []
    
    def niepoprawny_NIP(self, NIP):
        if (len(NIP) != 10):
            self.NIP = "Niepoprawny NIP!"
        else:
            self.NIP = NIP

    def zaciagnij_kredyt_firma(self, kwota):
        if self.saldo > kwota*2 and -1775 in self.historia:
            self.saldo += kwota
            return True
        return False
