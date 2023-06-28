import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-register-dandelion',
    templateUrl: './register-dandelion.component.html',
    styleUrls: ['./register-dandelion.component.css']
})
export class RegisterDandelionComponent {

    user = {
        name: '',
        username: '',
        email: '',
        password: ''
    };

    constructor(private http: HttpClient) { }

    registerUser(): void {
        this.http.post('/api/user/register', this.user).subscribe(
            response => {
                // Registro exitoso, manejar la respuesta del servidor
                console.log('Registro exitoso:', response);
            },
            error => {
                // Ocurrió un error durante el registro, manejar el error
                console.error('Error durante el registro:', error);
            }
        );
    }
}
