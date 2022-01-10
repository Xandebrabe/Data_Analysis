var fundo = window.document.body;
var botao = window.document.getElementById("botao");
var cont = 0;


function clicar(){
    cont++;
    if(cont == 1){
        fundo.style.backgroundColor = "#E6E7ED";
        botao.style.backgroundColor = "aqua";
    }
    else{
        cont = 0;
        fundo.style.backgroundColor = "#E1FAEE";
        botao.style.backgroundColor = "rgb(200, 200, 37)";
    }
}