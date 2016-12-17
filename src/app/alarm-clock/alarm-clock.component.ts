import {AlarmClockService} from "./alarm-clock.service";
import { Component, OnInit } from '@angular/core';
import { AlarmClock } from './alarm-clock';


@Component({
  selector: 'app-alarm-clock',
  templateUrl: './alarm-clock.component.html',
  styleUrls: ['./alarm-clock.component.css']
})
export class AlarmClockComponent implements OnInit {

  alarmclocks: AlarmClock[] = [];

  constructor(
    private alarmClockService: AlarmClockService
  ) { }

  ngOnInit() {
    this.alarmclocks = this.alarmClockService.getAllAlarmClocks();
    console.log(this.alarmclocks);
  }

  deleteAlarmClock(alarmclock){
    console.log(alarmclock)
    this.alarmClockService.deleteAlarmClockById(alarmclock.id)
    this.alarmclocks = this.alarmClockService.getAllAlarmClocks();
  }


}
