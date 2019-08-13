%rebase('osnova.tpl')

<h1>Vaše karte so:</h1>
%for el in roka: 
        <img src="https://deckofcardsapi.com/static/img/{{str(el).replace('T','0')}}.png"/>
    
% end
<h1>Karte so vam prinesle {{bonus}} €.</h1>
<h1>Vaše stanje na računu je {{stanje}} €</h1>
<form action="/vprasaj/" method="post">
        <input class="button" type="submit" value="NAPREJ">
</form>
