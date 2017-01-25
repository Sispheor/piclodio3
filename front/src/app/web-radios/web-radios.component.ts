import { Component, OnInit } from '@angular/core';
import { WebRadioService } from './web-radio.service';
import { WebRadio } from './web-radio';

@Component({
  selector: 'app-web-radios',
  templateUrl: './web-radios.component.html',
  styleUrls: ['./web-radios.component.css']
})
export class WebRadiosComponent implements OnInit {

  webradios: WebRadio[] = [];
  webRadioToDelete: WebRadio;
  modalConfirmDeleteWebRadioIsVisible: Boolean = false;
  message: String;

  constructor(private webRadioService: WebRadioService) { }

  ngOnInit() {
    this.webRadioService.getAllWebRadios().subscribe(this.filterDefaultWebRadio.bind(this));
  }

  deleteWebRadio(webradio){
    console.log(webradio);
    this.webRadioService.deleteWebRadioById(webradio.id);
    // this.webradios = this.webRadioService.getAllWebRadios();
  }

  confirmDeleteWebRadio(webradio){
      console.log("confirmDeleteWebRadio clicked");
      this.modalConfirmDeleteWebRadioIsVisible = true;
      this.webRadioToDelete = webradio;
      this.message = "Are you sure you want to delete " + this.webRadioToDelete.name
  }

  onConfirm(agreed: boolean) {
    this.modalConfirmDeleteWebRadioIsVisible = false;
    if (agreed){
      this.deleteWebRadio(this.webRadioToDelete);
    } 
  }

  filterDefaultWebRadio(webradios: WebRadio[]){
      console.log(webradios);
      this.webradios = webradios;
  }


}
