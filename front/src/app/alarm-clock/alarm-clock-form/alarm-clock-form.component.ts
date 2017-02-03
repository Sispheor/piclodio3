import { PopupComponent } from './../../popup/popup.component';
import { error } from 'util';
import { AlarmClock } from './../alarm-clock';
import {AlarmClockService} from "../alarm-clock.service";
import {WebRadioService} from "../../web-radios/web-radio.service";
import {WebRadio} from "../../web-radios/web-radio";
import { Component, OnInit, ViewChild } from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router'
import {Subscription } from 'rxjs';

@Component({
  selector: 'app-alarm-clock-form',
  templateUrl: './alarm-clock-form.component.html',
  styleUrls: ['./alarm-clock-form.component.css']
})
export class AlarmClockFormComponent implements OnInit {

  newAlarmClock: AlarmClock = new AlarmClock();
  webradios: WebRadio[];
  alarmclocks: AlarmClock[];
  existingAlarmClock: boolean = true;
  timePicker: Date;
  @ViewChild(PopupComponent) popupComponent: PopupComponent;

  // list of availlable minutes & hours
  minute_list: number[];
  hour_list: number[];
  private subscription: Subscription;

  constructor(private webRadioService: WebRadioService,
    private alarmClockService: AlarmClockService,
    private router: Router,
    private activatedRoute: ActivatedRoute) {
    this.minute_list = this.create_range(59);
    this.hour_list = this.create_range(23);
  }

  ngOnInit() {
    // get the id in the URL
    this.subscription = this.activatedRoute.params.subscribe(
      (param: any) => {
        let alarmClockId = param['id'];
        console.log(alarmClockId);
        if (!alarmClockId) {
          console.log("no id");
          this.existingAlarmClock = false;
          this.timePicker= new Date()
          return
        } else {
          console.log("get an id");
          // we have an ID, load the object from it
          this.alarmClockService.getAlarmClockById(alarmClockId).subscribe(
            this.setExistingAlarmClock.bind(this),
            error => console.error('Error: ' + error),
            () => console.log('Completed! Get an alarm ' + this.newAlarmClock.webradio));
        }
      });

    // get the list of WebRadio
    this.webRadioService.getAllWebRadios().subscribe(this.setWebRadios.bind(this))
  }

  onSubmit() {
    console.log("alarms form: onSubmit clicked")
    if (this.existingAlarmClock) {
      // get hours and minutes for the date picker. the backend want integer for each
      this.newAlarmClock.hour = this.timePicker.getHours();
      this.newAlarmClock.minute = this.timePicker.getMinutes();
      if (this.dayOfWeekChecked()){
        console.log("Alarm clock already exist, updating it with val" + this.newAlarmClock);
        this.alarmClockService.updateAlarmClockById(this.newAlarmClock.id, this.newAlarmClock).subscribe(
          success => {
            this.router.navigate(["alarms"]);
          },
          error => console.log("Error "+ error)
        );
      }else{
        // show error
        this.popupComponent.add('danger', 'You must select at least one day of week');
      }

    } else {
      console.log(this.timePicker);
      this.newAlarmClock.hour = this.timePicker.getHours();
      this.newAlarmClock.minute = this.timePicker.getMinutes();
      if (this.dayOfWeekChecked()){
        this.alarmClockService.addAlarmClock(this.newAlarmClock).subscribe(
          success => {
            this.router.navigate(["alarms"]);
          },
          error => console.log("Error " + error)
        );;
      }else{
        this.popupComponent.add('danger', 'You must select at least one day of week');
      }
    }

  }

  create_range(maxVal: number): number[] {
    var x = [];
    var i = 0;
    while (x.push(i++) <= maxVal) {};
    return x;
  }

  setWebRadios(webradios: WebRadio[]) {
    console.log(webradios);
    this.webradios = webradios;
  }

  setExistingAlarmClock(alarmClock: AlarmClock){
    this.newAlarmClock = alarmClock;
    this.timePicker = new Date();
    this.timePicker.setHours(this.newAlarmClock.hour);
    this.timePicker.setMinutes(this.newAlarmClock.minute);
  }

  dayOfWeekChecked(){
    if (this.newAlarmClock.monday || this.newAlarmClock.tuesday || this.newAlarmClock.wednesday || this.newAlarmClock.thursday ||
        this.newAlarmClock.friday || this.newAlarmClock.saturday || this.newAlarmClock.sunday){
          console.log("day of week ok");
      return true;
    }
    return false;
  }


}
