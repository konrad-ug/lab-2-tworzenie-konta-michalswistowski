class Konto:
    def __init__(self, imie, nazwisko, pesel, promocja = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.promocja = promocja

        self.warunek_peselu(pesel)
        self.warunek_promocji(promocja)

    def warunek_peselu(self, pesel):
        if(len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "niepoprawny pesel"
    
    def warunek_promocji(self, promocja):
        if(promocja != None and len(promocja) == 8 and promocja[:5] == "PROM_" and (int(self.pesel[:2]) > 60 or
        int(self.pesel[2:4]) > 20)): 
            self.saldo += 50
