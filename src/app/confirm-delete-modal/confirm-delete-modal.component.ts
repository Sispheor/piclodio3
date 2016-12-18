import {WebRadio} from "../web-radios/web-radio";
import { Component, Input, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-confirm-delete-modal',
  templateUrl: './confirm-delete-modal.component.html',
  styleUrls: ['./confirm-delete-modal.component.css']
})
export class ConfirmDeleteModalComponent {

  @Input() message: String;
  @Input() modalConfirmDeleteIsVisible: Boolean;
  @Output() onConfirm = new EventEmitter<boolean>();

  constructor() { }

  ngOnInit() {

  }

  canceldeleteWebRadio(){
    this.modalConfirmDeleteIsVisible = false;
    this.onConfirm.emit(false);
  }

  confirmDeleteWebRadio(){
    this.modalConfirmDeleteIsVisible = false;
    this.onConfirm.emit(true);

  }



}
