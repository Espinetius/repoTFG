import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-login-dandelion',
    templateUrl: './login-dandelion.component.html',
    styleUrls: ['./login-dandelion.component.css']
})
export class LoginDandelionComponent implements OnInit {
    @Output() registerClicked: EventEmitter<void> = new EventEmitter<void>();
    @Output() loggingClicked: EventEmitter<void> = new EventEmitter<void>();
    mail!: string;
    password!: string;
    errorMessage: string = '';

    constructor(private http: HttpClient) {
    }

    ngOnInit(): void {

    }

    logbySessionStorage() {
        if (sessionStorage.getItem("loged") == "true") {
            window.open("", "_self");
        } else {
            window.open("", "_self");
        }
    }
    onRegisterClick() {
        this.registerClicked.emit();
    }
    onLoggingClick() {
        this.loggingClicked.emit();
    }
    loggin(): void {
        const loginData = JSON.stringify({ mail: this.mail, password: this.password });

        this.http.post('/login', loginData).subscribe(
            (response: any) => {
                if (response.exists) {
                    sessionStorage.setItem("loged", 'true');
                    sessionStorage.setItem('actualUser', this.mail);
                    console.log(this.mail + 'se ha logeado correctamente');
                    window.location.href = "/home";
                } else {
                    this.showAlert('Invalidos Email o Password');
                }
            },
            (error: any) => {
                this.showAlert('Introduce los datos en los campos correspondientes')
            }
        )
    }
    showAlert(message: string) {
        this.errorMessage = message;
    }
}
