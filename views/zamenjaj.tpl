%rebase('osnova.tpl')

<form action="/zamenjaj/ "method="post">
    <h1>Vaše karte so:</h1>
    <ol>
%for el in roka: 
        <li>{{el}}</li>
%end
    </ol>
    <h1>Vpišite zaporedne številke kart, ki jih želite zamenjati.</h1>
    <h2>Zapišite jih brez vejic.</h2>
    <input class="input is-danger" name="pozicije" type="text">
</form>
