%rebase('osnova.tpl')


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
                <form action="/deposit/" method="post">
                    <div class="field">
                    <div class="control">
                        <h1>Koliko evrov želite položiti na svoj račun?</h1>
                        <input class="input is-danger" name="deposit" type="text" placeholder="Polog">
                    </div>
                    </div>
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
