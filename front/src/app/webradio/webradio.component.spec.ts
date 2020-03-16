import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WebradioComponent } from './webradio.component';

describe('WebradioComponent', () => {
  let component: WebradioComponent;
  let fixture: ComponentFixture<WebradioComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WebradioComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WebradioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
