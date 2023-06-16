window.addEventListener("load", iniciar);
let aux=[];

function iniciar(){
    document.getElementById("inicio").addEventListener("click", inicio);
    document.getElementById("resgister").addEventListener("click", abrirIndexUser);


    if(sessionStorage.getItem("logeo")=="true"){
        window.open("indexuser.html","_self");
    }
}

function inicio(){
    window.open("login.html", "_self");
}

function abrirIndexUser(){
    window.open("indexuser.html", "_self");
}

