import { Component, OnInit } from '@angular/core';
import { AlarmClock } from './alarm-clock';
import { WebRadio } from '../web-radios/web-radio';
import { WebRadioService } from '../web-radios/web-radio.service';


@Component({
  selector: 'app-alarm-clock',
  templateUrl: './alarm-clock.component.html',
  styleUrls: ['./alarm-clock.component.css']
})
export class AlarmClockComponent implements OnInit {

  webradios: WebRadio[] = [];
  newAlarmClock: AlarmClock = new AlarmClock();

  constructor(
    private webRadioService: WebRadioService
  ) { }

  ngOnInit() {
    this.webradios = this.webRadioService.getAllWebRadios();     
  }

  onSubmit() { 
    console.log(this.newAlarmClock)
  }


}
