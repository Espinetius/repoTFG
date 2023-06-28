import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderDandelionComponent } from './header-dandelion.component';

describe('HeaderDandelionComponent', () => {
  let component: HeaderDandelionComponent;
  let fixture: ComponentFixture<HeaderDandelionComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [HeaderDandelionComponent]
    });
    fixture = TestBed.createComponent(HeaderDandelionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
