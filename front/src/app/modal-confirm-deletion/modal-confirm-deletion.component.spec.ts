import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalConfirmDeletionComponent } from './modal-confirm-deletion.component';

describe('ModalConfirmDeletionComponent', () => {
  let component: ModalConfirmDeletionComponent;
  let fixture: ComponentFixture<ModalConfirmDeletionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModalConfirmDeletionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModalConfirmDeletionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
