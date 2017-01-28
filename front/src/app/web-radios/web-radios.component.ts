import { error } from 'util';
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
    this.refreshWebRadioList();
  }

  deleteWebRadio(webRadioToDelete){
    console.log("Deleting" + webRadioToDelete);
    this.webRadioService.deleteWebRadioById(webRadioToDelete.id).subscribe(success => this.refreshWebRadioList(),
                                                                            error => console.log("error: " + error))
    
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

  setWebRadios(webradios: WebRadio[]){
      console.log(webradios);
      this.webradios = webradios;
  }

  refreshWebRadioList(){
      console.log("Refresh the web radio list");
        this.webRadioService.getAllWebRadios().subscribe(this.setWebRadios.bind(this));
    }


}
