<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Poker Slots</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  
  <style>
    #kvote {
        margin: 0 auto;
        border-collapse: separate;
        border-spacing: 30px 0;
    }

    #kvote td {
        margin: 0 auto;
    }

  </style>
  
  </head>
  <body align="center">
    <div class="tile is-parent">
  <article class="tile is-child notification is-danger">
    <div class="content">
    {{!base}}
    </div>            
  </article>
</div>

Kvote za kombinacije:
<table id="kvote">
  <tr>
    <td>Par (samo za par Jackov ali boljše) - 1x</td>
    <td>Dva para - 2x</td> 
    <td>Tris (tri enake vrednosti)- 3x</td>
  </tr>
  <tr>
    <td>Lestvica (5 zaporednih kart)- 4x</td>
    <td>Barva (vse karte iste barva)- 5x</td> 
    <td>Full house (en par in en tris)- 8x</td>
  </tr>
  <tr>
    <td>Poker (štiri iste vrednosti)- 25x</td>
    <td>Barvna lestvica - 50x</td> 
    <td>Royal flush (barvna lestvica od T do A) - 250x</td>
  </tr>
</table>
  </body>
</html>