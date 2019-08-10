% rebase('osnova.tpl')

<div class="tile is-ancestor">
  <div class="tile is-vertical is-8">
    <div class="tile">
      <div class="tile is-parent is-vertical">
        <article class="tile is-child">

        </article>
        <article class="tile is-child">

        </article>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child notification is-danger">
            <div class="content">
                <form action="/naprej1/" method="POST">
            <h1>
                <input type="radio" name="glas1" value="da">
                    Moram pokukati v navodila
            </h1>
            <h1>
                <input type="radio" name="glas1" value="ne">
                    Želim igrati
            </h1>
            <h1>
                <input class="button" type="submit" value="Sprejmi odločitev">
            </h1>
        </form>
            </div>
        </article>
      </div>
    </div>
    <div class="tile is-parent">
      <article class="tile is-child">
      </article>
    </div>
  </div>
  <div class="tile is-parent">
    <article class="tile is-child">
    </article>
  </div>
</div>
