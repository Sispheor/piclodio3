import { AlarmClock } from './../alarm-clock';
import {AlarmClockService} from "../alarm-clock.service";
import {WebRadioService} from "../../web-radios/web-radio.service";
import {WebRadio} from "../../web-radios/web-radio";
import { Component, OnInit } from '@angular/core';
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
      this.newAlarmClock.hour = this.timePicker.getHours();
      this.newAlarmClock.minute = this.timePicker.getMinutes();
      console.log("Alarm clock already exist, updating it with val" + this.newAlarmClock);
      this.alarmClockService.updateAlarmClockById(this.newAlarmClock.id, this.newAlarmClock).subscribe(
        success => {
          this.router.navigate(["alarms"]);
        },
        error => console.log("Error "+ error)
      );
    } else {
      console.log(this.timePicker);
      this.newAlarmClock.hour = this.timePicker.getHours();
      this.newAlarmClock.minute = this.timePicker.getMinutes();
      this.alarmClockService.addAlarmClock(this.newAlarmClock).subscribe(
        success => {
          this.router.navigate(["alarms"]);
        },
        error => console.log("Error " + error)
      );;

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


}
