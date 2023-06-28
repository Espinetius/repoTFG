import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterDandelionComponent } from './register-dandelion.component';

describe('RegisterDandelionComponent', () => {
  let component: RegisterDandelionComponent;
  let fixture: ComponentFixture<RegisterDandelionComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RegisterDandelionComponent]
    });
    fixture = TestBed.createComponent(RegisterDandelionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
