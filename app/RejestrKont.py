# from app.Konto import Konto

class RejestrKont:

    lista = []

    @classmethod
    def dodaj(cls, konto):
        RejestrKont.lista.append(konto)

    @classmethod
    def szukaj(cls, pesel):
        for konto in RejestrKont.lista:
            if konto.pesel == pesel:
                return konto


    @classmethod
    def iloscKont(cls):
        return len(RejestrKont.lista)