import model
from model import Igralec, Karta, Hand





def polog_denarja():
    print('Koliko denarja želite položiti za mizo?')
    denar = input('> ')
    if model.preveri_ce_je_stevilka(denar):
        igralec = model.naredi_igralca(denar)
        return igralec
    else:
        print('Vaša izbira je neveljavna!')
        polog_denarja()

def stava():
    print('Koliko denarja želite staviti?')
    denar = input('> ')
    if model.preveri_ce_je_stevilka(denar):
        roka = model.nova_roka(denar)
        return roka
    else:
        print('Vaša izbira je neveljavna!')
        stava()

    



def igra():
    stava()


def intro():
    print('Pozdravljeni v moji bedni igri!')
    print('Porabite čim več denarja ker ga dobim jaz')
    polog_denarja()

def main():
    intro()
    while True:
        igra()

main()
