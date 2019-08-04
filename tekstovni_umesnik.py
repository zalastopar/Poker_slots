import model
from model import Igralec, Karta, Hand
import time




def polog_denarja():
    print('Koliko denarja želite vstaviti v avtomat?')
    denar = input('> ')
    if model.preveri_ce_je_stevilka(denar) == 'ja':
        igralec = model.naredi_igralca(denar)
        return igralec
    else:
        print('Vaša izbira je neveljavna!')
        return polog_denarja()

def stava(igralec):
    print('Koliko denarja želite staviti?')
    denar = input('> ')
    if model.preveri_ce_je_stevilka(denar) == 'ja':
        if model.preveri_ce_je_dovolj_denarja(igralec, denar):
            time.sleep(0.5)
            roka = model.nova_roka(denar)
            return roka
        else: 
            print('Na vašem računu ni dovolj denarja!')
            return stava(igralec)
    else:
        print('Vaša izbira je neveljavna!')
        return stava(igralec)

def zamenjaj_karte(roka):
    print('Zapišite mesta kart, ki jih želite zamenjati!')
    print('Zapišite jih, kot število.')
    pozicija = input('> ')
    if model.preveri_ce_so_karte_pravilno_vnesene(pozicija):
        roka = model.izloci_karte(roka, pozicija)
        model.dodaj_karte(roka)
        time.sleep(0.5)
        print(roka)
    else:
        print('Vaša izbira je neveljavna!')
        print('Vpišite mesta kart brez presledkov, npr: 23')
        zamenjaj_karte(roka)


def ali_zelite_menjati_karte(roka):
    print('Ali želite zamenjati katero od svojih kart?')
    odgovor = input('> ')
    odgovor = model.preveri_ja_ali_ne(odgovor)
    if odgovor == 'ja':
        zamenjaj_karte(roka)
    elif odgovor == 'ne':     
        pass
    else:
        print('Vaša izbira je neveljavna!')
        print('Vpišite da ali ne.')
        ali_zelite_menjati_karte(roka)

def ali_zelite_nadaljevati_igro(igralec):
    print('Ali želite ponovno staviti?')
    odgovor = input('> ')
    odgovor = model.preveri_ja_ali_ne(odgovor)
    if odgovor == 'ja':
        igra(igralec)
    elif odgovor == 'ne':     
        print('Hvala za igro!')
        return False
    else:
        print('Vaša izbira je neveljavna!')
        print('Vpišite da ali ne.')
        ali_zelite_nadaljevati_igro(igralec)
    
def zmanjkalo_denarja():
    print('Zmanjkalo vam je denarja.')
    print('Ali želite še kaj denarja naložiti?')
    odgovor = input('> ')
    odgovor = model.preveri_ja_ali_ne(odgovor)
    if odgovor == 'ja':
        igralec = polog_denarja()
        igra(igralec)
    elif odgovor == 'ne':    
        print('Hvala za igro!')
        return False
    else:
        print('Vaša izbira je neveljavna!')
        print('Vpišite da ali ne.')
        zmanjkalo_denarja()


def igra(igralec):
    roka = stava(igralec)
    print(roka)
    ali_zelite_menjati_karte(roka)
    bonus = model.doloci_bonus(roka)
    print('Vaše karte so vam prinesle ' + str(bonus) + ' €')
    model.spremeni_stanje(igralec, roka, bonus)
    print(igralec)
    if model.preveri_koliko_denarja(igralec):
        odgovor = zmanjkalo_denarja()
        return odgovor
    else:
        odgovor = ali_zelite_nadaljevati_igro(igralec)
        return odgovor

def pokazi_navodila():
    with open('navodila.txt', 'r', encoding = 'utf-8') as pravila:
        for vrstica in pravila:
            print(vrstica[:-1])
        

def zacetni_meni():
    print('Kaj želite storiti?')
    print('1) Moram pokukati v navodila')
    print('2) Želim igrati!')
    odgovor = input('> ')
    odgovor = model.preveri_ce_je_ena_ali_dva(odgovor)
    if odgovor == 'ena':
        pokazi_navodila()
        time.sleep(5)
        zacetni_meni()
    elif odgovor == 'dva':
        pass
    else:
        print('Vaš odgovor je neveljaven!')
        print('Vpišite 1 ali 2')
        zacetni_meni()
    


def intro():
    print('Pozdravljeni v moji super igri!')
    print('Porabite čim več denarja, ker ga dobim jaz.')
    zacetni_meni()
    igralec = polog_denarja()
    if model.preveri_koliko_denarja(igralec):
        zmanjkalo_denarja()
        return False
    else:
        pass
    return igralec
    


def main():
    igralec = intro()
    if not igralec:
        pass
    else:
        while True:
            if not igra(igralec):
                break
            else:
                continue

main()
