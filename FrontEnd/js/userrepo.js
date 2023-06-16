window.addEventListener("load",iniciar);

function iniciar(){
    document.getElementById("inicio").addEventListener("click", inicio);
    document.getElementById("login").addEventListener("click", login);
    
    if(sessionStorage.getItem("logeo")=="true"){
        window.open("indexuser.html","_self");
    }
}


function previewer(){
    const fileList = document.getElementById('fileList');
        const preview = document.getElementById('preview');

        fileList.addEventListener('click', function(event) {
        if (event.target.tagName === 'LI') {
            const file = event.target.dataset.file;
            preview.style.backgroundImage = `url(${file})`;
        }
        });
}

function abrirBusqueda(){
    select = "busquedaTexto";
    sessionStorage.setItem("select", select);
    sessionStorage.setItem("texto", document.getElementById("your-repos-filter").value);
    window.open("userrepo.html", "_self");
}

function inicio(){
    if(sessionStorage.getItem("logeo")=="true"){
        window.open("indexuser.html","_self");
    }
}