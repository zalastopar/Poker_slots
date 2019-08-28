import random


class Karta:

    def __init__(self, vrednost, barva):
        self.vrednost = vrednost
        self.barva = barva

    def __str__(self):
        return '{0}{1}'.format(self.vrednost, self.barva)

    def __repr__(self):
        return '{0}{1}'.format(self.vrednost, self.barva)

    def __eq__(self, other):
        return self.vrednost == other.vrednost and self.barva == other.barva



def naredi_karto():
    barve = ['C', 'D', 'H', 'S']
    vrednosti = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return Karta(random.choice(vrednosti), random.choice(barve))

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
        nov_sez.append(int(el))
    return sorted(nov_sez)

class Hand:

    def __init__(self, stava):
        roka = []
        while len(roka) < 5:
            karta = naredi_karto()
            if karta not in roka:
                roka += [karta]
        self.roka = roka
        self.stava = float(stava)

    def __str__(self):
        tekst = ''
        for el in self.roka:
            tekst += ' ' +str(el)
        return 'Vaše karte so:' + tekst 

    def __repr__(self):
        tekst = ''
        for el in self.roka:
            tekst += ' ' +str(el)
        return 'Vaše karte so:' + tekst 

    def pridobi_vrednosti(self):
        sez_vrednosti = []
        for el in self.roka:
            sez_vrednosti.append(el.vrednost)
        return sez_vrednosti

    def pridobi_barve(self):
        sez_barv = []
        for el in self.roka:
            sez_barv.append(el.barva)
        return sez_barv

    def izloci_in_dodaj_karte(self, pozicija):
        roka = self.roka
        pozicija1 = []
        stare_karte = []
        for el in pozicija:
            if el == ' ':
                pass
            else:
                pozicija1 += [el]
        pozicija1 = sorted(pozicija1)
        for el in pozicija1[::-1]:
            stare_karte.append(roka[int(el) -  1])
            del roka[int(el) -  1]
        self.roka = roka
        while len(self.roka) < 5:
            karta = naredi_karto()
            if karta not in self.roka and karta not in stare_karte:
                self.roka += [karta]
        return self

    def preveri_par(self):
        sez_vrednosti = self.pridobi_vrednosti()
        for vr in sez_vrednosti:
            if sez_vrednosti.count(vr) == 2 and vr in 'JQKA':
                return True
        return False

    def preveri_dva_para(self):
        sez_vrednosti = self.pridobi_vrednosti()
        st_parov = 0
        for el in sez_vrednosti:
            if sez_vrednosti.count(el) == 2:
                st_parov += 1
        return (st_parov / 2) == 2

    def preveri_tris(self):
        sez_vrednosti = self.pridobi_vrednosti()
        for vr in sez_vrednosti:
            if sez_vrednosti.count(vr) == 3:
                return True
        return False

    def preveri_lestvico(self):
        sez_vrednosti = self.pridobi_vrednosti()
        sez_vrednosti = spremeni_slikice_v_stevilke(sez_vrednosti)
        sez_vrednosti = razvrsti_po_velikosti(sez_vrednosti)
        i = 0
        for el in sez_vrednosti:
            if sez_vrednosti[0] + i != el:
                return sez_vrednosti == [2, 3, 4, 5, 14]
            i += 1
        return True

    def preveri_barvo(self):
        sez_barv = self.pridobi_barve()
        return sez_barv.count(sez_barv[0]) == 5 

    def preveri_full_house(self):
        sez_vrednosti = self.pridobi_vrednosti()
        for vr in sez_vrednosti:
            if str(sez_vrednosti.count(vr)) not in '23':
                return False
        return True

    def preveri_poker(self):
        sez_vrednosti = self.pridobi_vrednosti()
        return sez_vrednosti.count(sez_vrednosti[0]) == 4 

    def preveri_barvno_lestvico(self):
        return self.preveri_barvo() and self.preveri_lestvico()

    def preveri_royal_flush(self):
        sez_vrednosti = self.pridobi_vrednosti()
        return self.preveri_barvo() and 'T' in sez_vrednosti and 'J' in sez_vrednosti and 'Q' in sez_vrednosti and 'K' in sez_vrednosti and 'A' in sez_vrednosti
    
    def doloci_bonus(self):
        stava = self.stava
        if self.preveri_royal_flush():
            return stava * 250
        elif self.preveri_barvno_lestvico():
            return stava * 50
        elif self.preveri_poker():
            return stava * 25
        elif self.preveri_full_house():
            return stava * 8
        elif self.preveri_barvo():
            return stava * 5
        elif self.preveri_lestvico():
            return stava * 4
        elif self.preveri_tris():
            return stava * 3
        elif self.preveri_dva_para():
            return stava * 2
        elif self.preveri_par():
            return stava
        else:
            return 0
    
class Igralec:

    def __init__(self, deposit):
        self.stanje = deposit
        self.stava = 0
        self.roka = Hand(self.stava)

    def __str__(self):
        return 'Vaše stanje je {0} €'.format(self.stanje)

    def __repr__(self):
        return 'Vaše stanje je {0} €'.format(self.stanje)

    def preveri_koliko_denarja(self):
        denar = self.stanje
        if denar == 0:
            return True
        else:
            return False
        
    def vzemi(self):
        self.stanje -= self.stava

    def dodaj(self, bonus):
        self.stanje += bonus






def preveri_ce_je_stevilka(stevilka):
    st_pik = 0
    if len(stevilka) == 0:
        return False
    for el in stevilka:
        if el == ' ':
            return False
        elif el in '1234567890':
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
    

def preveri_ce_je_dovolj_denarja(igralec, denar):
    if igralec.stanje - denar >= 0:
        return True
    else:
        return False

def naredi_igralca(denar):
    igralec = Igralec(denar)
    return igralec

def nova_roka(denar):
    roka = Hand(denar)
    return roka

def preveri_ce_so_karte_pravilno_vnesene(karte):
    if len(karte) == 0:
        return False
    for el in karte:
        if el == ' ':
            return False
        elif el in '12345' and karte.count(el) == 1:
            continue
        else:
            return False
    return True

   

def preveri_ce_je_ena_ali_dva(odgovor):
    if odgovor == '1':
        return 'ena'
    elif odgovor == '2':
        return 'dva'
    elif len(odgovor) == 0:
        return 'narobe'
    else:
        return 'narobe'
    



