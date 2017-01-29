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

  modalConfirmDeleteAlarmClockIsVisible: Boolean = false;
  message: String;
  alarmClockToDelete: AlarmClock;

  constructor(
    private alarmClockService: AlarmClockService
  ) { }

  ngOnInit() {
    this.refreshAlarmClockList();        
  }

  deleteAlarmClock(alarmclock){
    // console.log(alarmclock)
    this.alarmClockService.deleteAlarmClockById(alarmclock.id).subscribe(success => this.refreshAlarmClockList(),
      error => console.log("error: " + error));

  }

  confirmDeleteAlarmClock(alarmclock: AlarmClock){
      console.log("confirmDeleteAlarmClock clicked");
      this.modalConfirmDeleteAlarmClockIsVisible = true;
      this.alarmClockToDelete = alarmclock;
      this.message = "Are you sure you want to delete the alarm \"" + this.alarmClockToDelete.name + "\""
  }

  onConfirm(agreed: boolean) {
    this.modalConfirmDeleteAlarmClockIsVisible = false;
    if (agreed){
      this.deleteAlarmClock(this.alarmClockToDelete);
    }
  }

  setAlarmClocks(alarmclocks: AlarmClock[]){
    this.alarmclocks = alarmclocks;
  }

  refreshAlarmClockList(){
      this.alarmClockService.getAllAlarmClocks().subscribe(this.setAlarmClocks.bind(this));
  }

}
