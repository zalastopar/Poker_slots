<html>
    <head>
        <title>Poker Slots</title>
    </head>
    <body>
        <h3>Vaše karte so:</h3>
        <ol>
%          for el in roka: 
            <li>{{el}}</li>
%          end
        </ol>
        <h3>Karte so vam prinesle {{bonus}} €.</h3>
        <h3>Vaše stanje na računu je {{stanje}} €</h3>
        <form action="/vprasaj/" method="post">
                <input type="submit" value="naprej">
        </form>
    </body>
</html>