<html>
    <head>
        <title>Poker Slots</title>
    </head>
    <body>
        <form action="/zamenjaj/ "method="post">
            <h3>Vaše karte so:</h3>
            <ol>
%           for el in roka: 
                <li>{{el}}</li>
%           end
            </ol>
            <h3>Vpišite zaporedne številke kart, ki jih želite zamenjati.</h3>
            <h4>Zapišite jih brez vejic.</h4>
            <input type="text" name="pozicije">
        </form>
    </body>
</html>