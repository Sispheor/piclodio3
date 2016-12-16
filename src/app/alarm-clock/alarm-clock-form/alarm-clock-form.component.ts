import {WebRadioService} from "../../web-radios/web-radio.service";
import {WebRadio} from "../../web-radios/web-radio";
import {AlarmClock} from "../alarm-clock";
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-alarm-clock-form',
  templateUrl: './alarm-clock-form.component.html',
  styleUrls: ['./alarm-clock-form.component.css']
})
export class AlarmClockFormComponent implements OnInit {

  newAlarmClock: AlarmClock = new AlarmClock();
  webradios : WebRadio[]

  constructor(private webRadioService: WebRadioService) {
    this.webradios = this.webRadioService.getAllWebRadios();
  }

  ngOnInit() {
  }

  onSubmit() {
    console.log(this.newAlarmClock)
  }

}
