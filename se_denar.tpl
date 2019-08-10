%rebase('osnova.tpl')
       
<h3>Vaše stanje na računu je {{stanje}} €</h3>
<h3>Kaj želite narediti?</h3>
<form action="/odlocitev/" method="post">
    <input type="radio" name="glas3" value="da">
        Želim še igrati
    <input type="radio" name="glas3" value="ne">
        Želim končati igro
    <input type="submit" value="sprejmi odločitev">
</form>
