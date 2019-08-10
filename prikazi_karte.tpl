<html>
    <head>
        <title>Poker Slots</title>
    </head>
    <body>
        <form action="/preveri_karte/" method="post">
            <h3>Vaše karte so:</h3>
            <ol>
%          for el in roka: 
                <li>{{el}}</li>
%          end
            </ol>
            <h4>Ali želite zamenjati katero od svojih kart?<h4>
            <input type="radio" name="glas2" value="da">
                Ja želim
            <input type="radio" name="glas2" value="ne">
                Ne želim
            <input type="submit" value="sprejmi odločitev">
        </form>
    </body>
</html>