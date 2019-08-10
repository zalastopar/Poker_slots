import bottle
import model
from model import Igralec, Hand, Karta

igralec = Igralec(0)

@bottle.get('/')
def pozdrav():
    return bottle.template('naslovna_stran.tpl')


@bottle.post('/naprej1/')
def prvi_meni():
    odgovor = bottle.request.forms['glas1']
    if odgovor == 'da':
        return bottle.template('navodila.tpl')
    else:
        bottle.redirect('/polozi_denar/')


@bottle.get('/polozi_denar/')
def polozi_denar():
    return bottle.template('deposit.tpl')


@bottle.post('/deposit/')
def polozi_denar():
    denar = bottle.request.forms['deposit']
    if model.preveri_ce_je_stevilka(denar):
        denar = float(denar)
        if denar == 0:
            return bottle.template('ni_denarja.tpl')
        else:
            igralec.stanje = denar
            return bottle.redirect('/stavi/')
    else:
        return bottle.template('neveljavna_izbira.tpl', link='/polozi_denar/') 

@bottle.get('/stavi/')
def stavi():
    return bottle.template('vprasanje_za_stavo.tpl', stanje = igralec.stanje)

@bottle.post('/preveri_stavo/')
def preveri():
    stava = bottle.request.forms['stava']
    if model.preveri_ce_je_stevilka(stava):
        stava = float(stava)
        if stava == 0:
            return bottle.template('stava0.tpl')
        elif model.preveri_ce_je_dovolj_denarja(igralec, stava):
            igralec.stava = stava
            return bottle.redirect('/nova_roka/')
        else:
            return bottle.template('napacna_stava.tpl')
    else:
        return bottle.template('neveljavna_izbira.tpl', link = '/stavi/')

@bottle.get('/nova_roka/')
def nova_roka():
    roka = model.nova_roka(igralec.stava)
    igralec.roka = roka
    return bottle.template('prikazi_karte.tpl', roka = roka.roka)

@bottle.post('/preveri_karte/')
def preveri_karte():
    odgovor = bottle.request.forms['glas2']
    if odgovor == 'da':
        return bottle.redirect('/menjava/')
    else:
        return bottle.redirect('/nove_karte/')

@bottle.get('/menjava/')
def menjava():
    roka = igralec.roka
    return bottle.template('zamenjaj.tpl', roka = roka.roka)

@bottle.post('/zamenjaj/')
def zamenjaj():
    roka = igralec.roka
    pozicija = bottle.request.forms['pozicije']
    if model.preveri_ce_so_karte_pravilno_vnesene(pozicija):
        roka = roka.izloci_in_dodaj_karte(pozicija)
        return bottle.redirect('/nove_karte/')
    else:
        return bottle.template('neveljavna_izbira.tpl', link = '/menjava/')

@bottle.get('/nove_karte/')
def nove():
    roka = igralec.roka
    roka.stava = igralec.stava
    bonus = model.doloci_bonus(roka)
    model.spremeni_stanje(igralec, roka, bonus)
    return bottle.template('pokazi_bonus.tpl', roka = roka.roka, bonus = bonus, stanje = igralec.stanje)

@bottle.post('/vprasaj/')
def vprasaj():
    if not model.preveri_koliko_denarja(igralec):
        return bottle.template('se_denar.tpl', stanje = igralec.stanje)
    else:
        return bottle.template('ni_denarja.tpl')


@bottle.post('/odlocitev/')
def odlocitev():
    odgovor = bottle.request.forms['glas3']
    if odgovor == 'da':
        return bottle.redirect('/stavi/')
    elif odgovor == 'ne':
        return bottle.redirect('/konec/')        
    else:
        return bottle.redirect('/polozi_denar/')

@bottle.post('/skoraj/')
def skoraj():
    odgovor = bottle.request.forms['konec']
    if odgovor == 'ne':
        return bottle.redirect('/konec/')       
    else:
        return bottle.redirect('/stavi/')


@bottle.get('/konec/')
def konec():
    return bottle.template('konec.tpl', stanje = igralec.stanje)



    



bottle.run(debug = True, reloader = True)
