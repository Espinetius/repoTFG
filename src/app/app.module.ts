import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';


import { AppComponent } from './app.component';
import { LoginDandelionComponent } from './login-dandelion/login-dandelion.component';
import { HeaderDandelionComponent } from './header-dandelion/header-dandelion.component';
import { FooterDandelionComponent } from './footer-dandelion/footer-dandelion.component';
import { RegisterDandelionComponent } from './register-dandelion/register-dandelion.component';
import { IndexComponent } from './index/index.component';
import { RepoComponent } from './repo/repo.component';
import { ConfigUserComponent } from './config-user/config-user.component';

@NgModule({
    declarations: [
        AppComponent,
        LoginDandelionComponent,
        HeaderDandelionComponent,
        FooterDandelionComponent,
        RegisterDandelionComponent,
        IndexComponent,
        RepoComponent,
        ConfigUserComponent
    ],
    imports: [
        BrowserModule,
        HttpClientModule,
        FormsModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
