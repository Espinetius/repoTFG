window.addEventListener("load", iniciar);

function iniciar() {
  document.getElementById("inicio").addEventListener("click", inicio);
  document.getElementById("resgister").addEventListener("click", abrirIndexUser);

  document.getElementById("registerForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(document.getElementById("registerForm"));
    const jsonData = {};

    for (const [key, value] of formData.entries()) {
      jsonData[key] = value;
    }

   fetch('/api/user/register', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: document.getElementById('nameRegister').value,
        username: document.getElementById('nameuserRegister').value,
        mail: document.getElementById('mailRegister').value,
        password: document.getElementById('passwordRegister').value
    })
})

  if (sessionStorage.getItem("logeo") == "true") {
    window.open("indexuser.html", "_self");
  }
}

function inicio() {
  window.open("login.html", "_self");
}

function abrirIndexUser() {
  window.open("indexuser.html", "_self");
}
