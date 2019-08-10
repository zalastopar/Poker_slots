%rebase('osnova.tpl')

<form action="/preveri_stavo/" method="post">
    <h3>Na vašem računu je {{stanje}} €.</h3>
    <h3>Koliko denarja želite staviti naslednje mešanje?</h3>
    <input type="text" name="stava">
</form>
