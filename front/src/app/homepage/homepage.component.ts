import { WebRadio } from './../web-radios/web-radio';
import { SystemDateService } from './systemdate.service';
import { Component, OnDestroy, OnInit } from '@angular/core';
import {SystemDate} from '../system-date';
import { WebRadioService } from '../web-radios/web-radio.service';
import { Observable, Subscription } from 'rxjs/Rx';


@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit, OnDestroy {
  clock: Date;
  active_webradios: any [];
  all_webradios: any [];
  systemDateSubscribption: Subscription;
  clockIncrementSubscription: Subscription;

  constructor(private webRadioService: WebRadioService, private systemDateService: SystemDateService) { 
   
    
  }

  ngOnInit() {
    this.systemDateSubscribption = this.systemDateService.getSystemDate().subscribe(this.setClockCallback.bind(this));
    
    //this.active_webradios = this.webRadioService.getAllWebRadios().filter(webradio => webradio.is_active)
    this.webRadioService.getAllWebRadios()                                                       
                            .subscribe(this.filterDefaultWebRadio.bind(this));
    
  }
  // subcribe return the target object
  setClockCallback(date: Date){
    this.clock = date;
    this.clockIncrementSubscription = Observable
                    .interval(1000)
                    .subscribe(this.incrementDate.bind(this));

  }

  incrementDate(){
    this.clock.setSeconds(this.clock.getSeconds() +1)
  }

  ngOnDestroy(){    
    this.systemDateSubscribption.unsubscribe();
    if (this.clockIncrementSubscription){
        this.clockIncrementSubscription.unsubscribe();
    }
    
  }

  /**
   * Filter the received list of webradios to keep only the active one (is_default)
   */
  filterDefaultWebRadio(webradios: WebRadio[]){
      this.all_webradios = webradios;
      console.log(webradios);
      this.active_webradios = this.all_webradios.filter(
        webradio => webradio.is_default === true
      )
  }

}
