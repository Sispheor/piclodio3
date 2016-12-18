import {WebRadio} from "../web-radios/web-radio";
import { Component, Input, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-confirm-delete-modal',
  templateUrl: './confirm-delete-modal.component.html',
  styleUrls: ['./confirm-delete-modal.component.css']
})
export class ConfirmDeleteModalComponent {

  @Input() message: String;
  @Input() webradioToDelete: WebRadio;
  @Input() modalConfirmDeleteWebRadioIsVisible: Boolean;
  @Output() onConfirm = new EventEmitter<boolean>();

  constructor() { }

  ngOnInit() {

  }

  canceldeleteWebRadio(){
    this.modalConfirmDeleteWebRadioIsVisible = false;
    this.onConfirm.emit(false);
  }

  confirmDeleteWebRadio(){
    this.modalConfirmDeleteWebRadioIsVisible = false;
    this.onConfirm.emit(true);

  }



}
