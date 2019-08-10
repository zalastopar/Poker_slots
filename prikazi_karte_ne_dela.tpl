<html>
    <form action="/zamenjaj/ "method="post">
        <h3>Vaše karte so:</h4>
        <h4>Odklukajte tiste, ki jih želite zamenjati!</h5>
%       i = 1
%       for el in roka: 
            <input type="checkbox" name="{{i}}" value="1">{{el}}
%           i += 1
%       end
        <input type="submit" value="Potrdi">
    </form>
</html>