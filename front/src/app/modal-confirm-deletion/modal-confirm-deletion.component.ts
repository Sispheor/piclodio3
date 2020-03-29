import { Component, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-modal-confirm-deletion',
  templateUrl: './modal-confirm-deletion.component.html',
  styleUrls: ['./modal-confirm-deletion.component.scss']
})
export class ModalConfirmDeletionComponent {

  @Input() name;

  constructor(public activeModal: NgbActiveModal) { }


}
