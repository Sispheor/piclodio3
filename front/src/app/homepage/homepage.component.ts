import { Component, OnInit } from '@angular/core';
import {SystemDate} from '../system-date';
import { WebRadioService } from '../web-radios/web-radio.service';
import {Observable} from 'rxjs/Rx';


@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  constructor(private webRadioService: WebRadioService) { 
    var all_webradios = this.webRadioService.getAllWebRadios();
    this.active_webradios = [];
    for (let webradio of all_webradios) {
      if (webradio.is_active){
        this.active_webradios.push(webradio)
      }
    }
  }

  ngOnInit() {
  }

  clock = Observable
        .interval(1000)
        .map(()=> new Date());

  active_webradios = this.active_webradios
  

}
