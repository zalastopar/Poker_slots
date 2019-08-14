%from model import Karta
%rebase('osnova_karte.tpl')

<form action="/preveri_karte/" method="post">
<h1>Vaše karte so:</h1>

%for el in roka: 
        <img src="https://deckofcardsapi.com/static/img/{{str(el).replace('T','0')}}.png"/>
    
% end

<h1>Ali želite zamenjati katero od svojih kart?<h1>
    <input class="button" type="submit" name="glas2" value="Ja">
    <input class="button" type="submit" name="glas2" value="Ne">
</form>

