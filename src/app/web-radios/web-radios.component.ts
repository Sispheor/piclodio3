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
  newWebradio: WebRadio = new WebRadio();

  constructor(private webRadioService: WebRadioService) { }

  ngOnInit() {
    this.webradios = this.webRadioService.getAllWebRadios();      
  }

  onSubmit() {     
    this.webRadioService.addWebRadio(this.newWebradio) 
    this.newWebradio = new WebRadio();
  }

  deleteWebRadio(webradio){
    console.log(webradio)
    this.webRadioService.deleteWebRadioById(webradio.id)
    this.webradios = this.webRadioService.getAllWebRadios();    
  }
  

}
