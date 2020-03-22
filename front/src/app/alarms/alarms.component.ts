import { Component, OnInit } from '@angular/core';
import { Alarm } from '../models/alarm';
import { AlarmsService } from '../services/alarms.service';

@Component({
  selector: 'app-alarms',
  templateUrl: './alarms.component.html',
  styleUrls: ['./alarms.component.scss']
})
export class AlarmsComponent implements OnInit {

  alarms: Alarm[] = [];


  constructor(private alarmsService: AlarmsService) { }

  ngOnInit(): void {
    this.refreshAlarmClockList();
  }

  refreshAlarmClockList() {
    this.alarmsService.getAlarms().subscribe(this.setAlarmClocks.bind(this));
  }

  setAlarmClocks(alarms: Alarm[]) {
    console.log(alarms)
    this.alarms = alarms;
  }

  switchAlarmStatus(alarm: Alarm){
    if (alarm.enabled) {
      alarm.enabled = false
    } else {
      alarm.enabled = true
    }
    // update the alarm
    this.alarmsService.updateAlarm(alarm).subscribe(
      success => {
        this.refreshAlarmClockList();
      },
      error => console.log("Error " + error)
    );
  }


}
