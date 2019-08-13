%rebase('osnova.tpl')

<form action="/preveri_stavo/" method="post">
    <h1>Na vašem računu je {{stanje}} €.</h1>
    <h1>Koliko denarja želite staviti naslednje mešanje?</h1>
    <input class="input is-danger" name="stava" type="text" placeholder="Stava">
</form>
