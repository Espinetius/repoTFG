window.addEventListener("load", iniciar);

function iniciar() {
  document.getElementById("inicio").addEventListener("click", inicio);
  document.getElementById("createAcc").addEventListener("click", register);

  if (sessionStorage.getItem("logeo") == "true") {
    window.open("indexuser.html", "_self");
  }

  document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Obtener los valores de correo electrónico y contraseña


    // Realizar una solicitud AJAX al servidor para verificar la existencia del usuario
    const request = new XMLHttpRequest();
    request.open("POST", "/login", true);
    request.setRequestHeader("Content-Type", "application/json");
    const mail = document.getElementById("mail").value;
    const password = document.getElementById("password").value;
    console.log(mail);
    console.log(password);
    request.onload = function () {
      if (request.status === 200) {
        const response = JSON.parse(request.responseText);
        if (response.exists) {
          sessionStorage.setItem("logeo", true);
          sessionStorage.setItem("actualUser", mail);
          window.open("indexuser.html", "_self");
        } else {
          showAlert("Invalid Email or Password");
        }
      } else {
        showAlert("An error occurred. Please try again later.");
      }
    };

    request.onerror = function () {
      showAlert("An error occurred. Please try again later.");
    };

    const data = JSON.stringify({ mail: mail, password: password });
    request.send(data);
  });
}

function showAlert(message) {
  const alertDiv = document.createElement("div");
  alertDiv.classList.add("alert", "alert-danger");
  alertDiv.textContent = message;

  const container = document.getElementById("loginForm");
  container.insertBefore(alertDiv, container.firstChild);
}

function inicio() {
  window.open("login.html", "_self");
}

function register() {
  window.open("register.html", "_self");
}
