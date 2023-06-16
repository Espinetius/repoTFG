window.addEventListener("load", iniciar);
let aux=[];

function iniciar(){
    document.getElementById("inicio").addEventListener("click", inicio);
    document.getElementById("login").addEventListener("click", login);
    document.getElementById("createAcc").addEventListener("click", register);


    if(sessionStorage.getItem("logeo")=="true"){
        window.open("indexuser.html","_self");
    }
}

function login(){
    const url = "users.json";
    fetch (url)
        .then (respuesta => respuesta.json())
        .then (json => cargarJSON(json))
        .catch(e => console.log(e));
}

function cargarJSON(myObj){
    for(i=0; i<myObj.length; i++){
        localStorage.setItem("user"+ myObj[i], aux);
    }
    usuario = document.getElementById("exampleInputEmail1").value;
    password = document.getElementById("exampleInputPassword1").value;

    if(sessionStorage.getItem("logeo")=="false"){
        for(i=0; i<myObj.length && sessionStorage.getItem("logeo")=="false";i++){
            if(myObj[i]['user']== usuario && myObj[i]['password']==password){
                sessionStorage.setItem("logeo", true);          
                sessionStorage.setItem("actualUser", usuario);
                window.open("indexuser.html", "_self");
            }
        }
        if(sessionStorage.getItem("logeo")=="false"){
            document.getElementById("aviso").innerHTML = "<p>Invalid Email or Password</p>";
        }
    }
}

function inicio(){
    window.open("login.html", "_self");
}

function register(){
    window.open("register.html", "_self");
}