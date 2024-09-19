/**
* O search retorna o indice da 
* primeira ocorrencia do padrao desejado.
* nesse caso o 10 não é visto como uma 
* coisa só e sim 1 e o próximo elemento 0
*/
function buscarNumero(dados){
    let resultado = dados.search(/\d/);
    return resultado;
}

function matchNumero(dados){
    const exp = /[0-9]/g;
    let resp = dados.match(exp);
    return resp;
}

window.addEventListener("load",
    function(){
        let buscarN = document.querySelector('#btnBuscarN');
        
        buscarN.addEventListener("click",
            function(){
                let idade = document.querySelector('#idade').value;
                if (idade != ""){
                    let resp = buscarNumero(idade);
                    alert("indice: "+resp+"\n"+
                          "primeiro numero: "+idade[resp]);
                    
                    resp = matchNumero(idade);
                    alert("indice: "+resp+"\n");
                }
                else{
                    alert ("O campo idade esta vazio")
                }
            }
        )
    }
)

/*
let d = "arroz, batata, lasanha10, paste4";
alert(d);

let resp =  buscarNumero(d);
alert("indice: "+resp+"\n"+
    "primeiro numero: "+d[0,resp]);
*/
