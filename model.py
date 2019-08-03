import random

class Igralec:

    def __init__(self, deposit):
        self.stanje = deposit

    def __str__(self):
        return 'Vaše stanje je {0} €'.format(self.stanje)

class Karta:

    def __init__(self, vrednost, barva):
        self.vrednost = vrednost
        self.barva = barva

    def __str__(self):
        return '{0}{1}'.format(self.vrednost, self.barva)

    def __repr__(self):
        return '{0}{1}'.format(self.vrednost, self.barva)


def naredi_karto():
    barve = ['C', 'D', 'H', 'S']
    vrednosti = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return Karta(random.choice(vrednosti), random.choice(barve))

class Hand:

    def __init__(self, stava):
        roka = []
        while len(roka) < 5:
            karta = naredi_karto()
            if karta not in roka:
                roka += [karta]
        self.roka = roka
        self.stava = stava

        
    def __str__(self):
        tekst = ''
        for el in self.roka:
            tekst += ' ' +str(el)
        return 'Vaše karte so:' + tekst 


def izloci_karte(hand, pozicija):
    roka = hand.roka
    for el in pozicija[::-1]:
        del roka[el]
    hand.roka = roka
    return hand

def dodaj_karte(hand):
    while len(hand.roka) < 5:
        karta = naredi_karto()
        if karta not in hand.roka:
            hand.roka += [karta]
    return hand

def preveri_ce_je_stevilka(stevilka):
    st_pik = 0
    for el in stevilka:
        if el in '1234567890':
            pass
        else:
            if el == '.':
                if st_pik == 0:
                    st_pik += 1
                else:
                    return False
            else:
                return False
    return True


def naredi_igralca(denar):
    igralec = Igralec(float(denar))
    return igralec

def nova_roka(denar):
    roka = Hand(float(denar))
    return roka



