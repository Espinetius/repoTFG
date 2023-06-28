import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginDandelionComponent } from './login-dandelion.component';

describe('LoginDandelionComponent', () => {
  let component: LoginDandelionComponent;
  let fixture: ComponentFixture<LoginDandelionComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LoginDandelionComponent]
    });
    fixture = TestBed.createComponent(LoginDandelionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
