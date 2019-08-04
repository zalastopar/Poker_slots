import random

class Igralec:

    def __init__(self, deposit):
        self.stanje = deposit

    def __str__(self):
        return 'Vaše stanje je {0} €'.format(self.stanje)


def spremeni_stanje(igralec, hand, bonus):
    if bonus == 0:
        igralec.stanje -= hand.stava
    else:
        igralec.stanje += bonus

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
        del roka[int(el) -  1]
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
    if len(stevilka) == 0:
        return False
    for el in stevilka:
        if el in '1234567890':
            pass
        else:
            if el == '.':
                if st_pik == 0:
                    st_pik += 1
                else:
                    return 'ne'
            else:
                return 'ne'
    return 'ja'

def preveri_ce_je_dovolj_denarja(igralec, denar):
    if igralec.stanje - float(denar) >= 0:
        return True
    else:
        return False

def naredi_igralca(denar):
    igralec = Igralec(float(denar))
    return igralec

def nova_roka(denar):
    roka = Hand(float(denar))
    return roka

def preveri_ce_so_karte_pravilno_vnesene(karte):
    if len(karte) == 0:
        return False
    for el in karte:
        if el in '12345' and karte.count(el) == 1:
            return True
        else:
            return False

def preveri_ja_ali_ne(odgovor):
    odgovor = odgovor.lower()
    if odgovor == 'ja' or odgovor == 'da':
        return 'ja'
    elif odgovor == 'ne':
        return 'ne'
    elif len(odgovor) == 0:
        return 'narobe'
    else:
        return 'narobe'
    
def preveri_par(hand):
    sez_vrednosti = []
    for el in hand.roka:
        sez_vrednosti += [el.vrednost]
    for vr in sez_vrednosti:
        if sez_vrednosti.count(vr) == 2 and vr in 'JQKA':
            return True
    return False


def preveri_dva_para(hand):
    sez_vrednosti = []
    st_parov = 0
    for el in hand.roka:
        sez_vrednosti += [el.vrednost]
    for el in sez_vrednosti:
        st = sez_vrednosti.count(el)
        if st == 2:
            st_parov += 1
    return (st_parov / 2) == 2
    
def preveri_tris(hand):
    sez_vrednosti = []
    for el in hand.roka:
        sez_vrednosti += [el.vrednost]
    for vr in sez_vrednosti:
        if sez_vrednosti.count(vr) == 3:
            return True
    return False

def spremeni_slikice_v_stevilke(sez):
    for el in sez:
        if el == 'J':
            sez = sez[0 : sez.index(el)] + ['11'] + sez[sez.index(el) + 1:]
        elif el == 'Q':
            sez = sez[0 : sez.index(el)] + ['12'] + sez[sez.index(el) + 1:]
        elif el == 'K':
            sez = sez[0 : sez.index(el)] + ['13'] + sez[sez.index(el) + 1:]
        elif el == 'A':
            sez = sez[0 : sez.index(el)] + ['14'] + sez[sez.index(el) + 1:]
        elif el == 'T':
            sez = sez[0 : sez.index(el)] + ['10'] + sez[sez.index(el) + 1:]
    return sez

def razvrsti_po_velikosti(sez):
    nov_sez = []
    for el in sez:
        nov_sez += [int(el)]
    return sorted(nov_sez)

def preveri_lestvico(hand):
    sez_vrednosti = []
    for el in hand.roka:
        sez_vrednosti += [el.vrednost]
    sez_vrednosti = spremeni_slikice_v_stevilke(sez_vrednosti)
    sez_vrednosti = razvrsti_po_velikosti(sez_vrednosti)
    zacetek = int(sez_vrednosti[0])
    return (zacetek + 1) in sez_vrednosti and (zacetek + 2) in sez_vrednosti and (zacetek + 3) in sez_vrednosti and (zacetek + 4) in sez_vrednosti

def preveri_barvo(hand):
    sez_barv = []
    for el in hand.roka:
        sez_barv += [el.barva]
    return sez_barv.count(sez_barv[0]) == 5 

def preveri_full_house(hand):
    sez_vrednosti = []
    for el in hand.roka:
        sez_vrednosti += [el.vrednost]
    for vr in sez_vrednosti:
        if str(sez_vrednosti.count(vr)) not in '23':
            return False
    return True

def preveri_poker(hand):
    sez_vrednosti = []
    for el in hand.roka:
        sez_vrednosti += [el.vrednost]
    return sez_vrednosti.count(sez_vrednosti[0]) == 5 

def preveri_barvno_lestvico(hand):
    return preveri_barvo(hand) and preveri_lestvico(hand)

def preveri_royal_flush(hand):
    sez_vrednosti = []
    for el in hand.roka:
        sez_vrednosti += [el.vrednost]
    return preveri_barvo(hand) and 'T' in sez_vrednosti and 'J' in sez_vrednosti and 'Q' in sez_vrednosti and 'K' in sez_vrednosti and 'A' in sez_vrednosti
    

def doloci_bonus(hand):
    stava = hand.stava
    if preveri_par(hand):
        return stava
    elif preveri_dva_para(hand):
        return stava * 2
    elif preveri_tris(hand):
        return stava * 3
    elif preveri_lestvico(hand):
        return stava * 4
    elif preveri_barvo(hand):
        return stava * 5
    elif preveri_full_house(hand):
        return stava * 8
    elif preveri_poker(hand):
        return stava * 25
    elif preveri_barvno_lestvico(hand):
        return stava * 50
    elif preveri_royal_flush(hand):
        return stava * 250
    else:
        return 0

def preveri_ce_je_ena_ali_dva(odgovor):
    if odgovor == '1':
        return 'ena'
    elif odgovor == '2':
        return 'dva'
    elif len(odgovor) == 0:
        return 'narobe'
    else:
        return 'narobe'
    
def preveri_koliko_denarja(igralec):
    denar = igralec.stanje
    if denar == 0:
        return True
    else:
        return False



