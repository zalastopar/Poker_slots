import bottle
import model
from model import Igralec, Karta, Hand

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
    bottle.template('deposit.tpl')
    denar = bottle.request.forms['deposit']
    if model.preveri_ce_je_stevilka(denar):
        denar = float(denar)
        igralec.stanje = denar
        return bottle.redirect('/stavi/')
    else:
        return bottle.template('neveljavna_izbira.tpl', link='/polozi_denar/') 

@bottle.get('/stavi/')
def stavi():
    return bottle.template('vprasanje_za_stavo.tpl', stanje = igralec.stanje)

    



bottle.run(debug = True, reloader = True)
