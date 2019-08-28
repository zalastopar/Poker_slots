%rebase('osnova_karte.tpl')

<style>
    #karte td {
        border: None;
    }
</style>


<form submit action="/zamenjaj/" method="post">
    <h1>Vaše karte so:</h1>
<table id="karte">

    <tr>
%i=1
%for el in roka: 
    <td>
        <img src="https://deckofcardsapi.com/static/img/{{str(el).replace('T','0')}}.png"/>
    </td>
% i += 1  
% end
    </tr>
    <tr>
%for i in range(1, 6):
    <td>
        <input type="checkbox" name="karta" value="{{i}}"/> 
    </td>
%end


  </tr>
</table>
    <h1>Označite karte, ki jih želite zamenjati.</h1>
    <input class="button" type="submit" name="glas1" value="Naprej">
</form>

