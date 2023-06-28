import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FooterDandelionComponent } from './footer-dandelion.component';

describe('FooterDandelionComponent', () => {
  let component: FooterDandelionComponent;
  let fixture: ComponentFixture<FooterDandelionComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FooterDandelionComponent]
    });
    fixture = TestBed.createComponent(FooterDandelionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
