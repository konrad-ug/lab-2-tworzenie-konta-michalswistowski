class Konto:
    def __init__(self, imie, nazwisko, pesel, promocja = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.promocja = promocja
        self.konto_biznesowe = False
        self.historia = []

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

    def zaksieguj_przelew_wychodzacy(self, przelew):
        if(self.saldo >= przelew):
            self.saldo -= przelew
            self.historia.append(-przelew)

    def zaksieguj_przelew_przychodzacy(self, przelew):
        self.saldo += przelew
        self.historia.append(przelew)

    def zaksieguj_przelew_ekspresowy(self, przelew):
        if self.saldo >= przelew:
            self.saldo -= przelew
            if self.konto_biznesowe == True:
                self.saldo -= 5
                self.historia.append(-przelew)
                self.historia.append(-5)
            else:
                self.saldo -= 1
                self.historia.append(-przelew)
                self.historia.append(-1)

    def zaciagnij_kredyt(self, kwota):
        sum = 0
        if (len(self.historia) < 3):
            return False
        if (self.historia[-3] > 0 and self.historia[-2] > 0 and self.historia[-1] > 0):
            self.saldo += kwota
            return True
        if (len(self.historia) < 5):
            return False
        for i in self.historia[-5:]:
            sum += i
        if (sum <= kwota):
            return False
        self.saldo += kwota
        return True


