%rebase('osnova.tpl')

<h1>Vaše karte so:</h1>
<ol>
% for el in roka: 
    <li>{{el}}</li>
%end
</ol>
<h1>Karte so vam prinesle {{bonus}} €.</h1>
<h1>Vaše stanje na računu je {{stanje}} €</h1>
<form action="/vprasaj/" method="post">
        <input class="button" type="submit" value="NAPREJ">
</form>
