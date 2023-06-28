import { Component } from '@angular/core';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    title = 'Dandelion';
    loggeado = false;
    showLogin = true;
    showRegistration = false;
    showIndex = true;
    showRepo = false;
    showConfigUser = false;


    switchToRegistration() {
        this.showLogin = false; // Ocultar el componente de inicio de sesión
        this.showRegistration = true; // Mostrar el componente de registro
    }
    switchLogged() {
        this.loggeado = true;
    }
    switchToIndex() {
        this.showIndex = true;
        this.showRepo = false;
        this.showConfigUser = false;
    }
    switchToRepo() {
        this.showIndex = false;
        this.showRepo = true;
        this.showConfigUser = false;
    }
    switchToConfigUser() {
        this.showIndex = false;
        this.showRepo = false;
        this.showConfigUser = true;
    }
}
