%rebase('osnova.tpl')
       
<h1>Vaše stanje na računu je {{stanje}} €</h1>
<h1>Ali želite igro nadaljevati?</h1>
<form action="/odlocitev/" method="post">
    <input class="button" type="submit" name="glas3" value="Ja">
    <input class="button" type="submit" name="glas3" value="Ne">
</form>
