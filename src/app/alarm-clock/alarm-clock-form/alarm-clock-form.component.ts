
import {AlarmClockService} from "../alarm-clock.service";
import {WebRadioService} from "../../web-radios/web-radio.service";
import {WebRadio} from "../../web-radios/web-radio";
import {AlarmClock} from "../alarm-clock";
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
  webradios : WebRadio[];
  alarmclocks: AlarmClock[];

  // list of availlable minutes & hours
  minute_list: number[];
  hour_list: number[];
  private subscription: Subscription;

  constructor(private webRadioService: WebRadioService,
              private alarmClockService: AlarmClockService,
              private router: Router,
              private activatedRoute: ActivatedRoute) {
    this.webradios = this.webRadioService.getAllWebRadios();
    this.alarmclocks = this.alarmClockService.getAllAlarmClocks();
    this.minute_list= this.create_range(59);
    this.hour_list= this.create_range(23);
  }

  ngOnInit() {
    // get the id in the URL
    this.subscription = this.activatedRoute.params.subscribe(
      (param: any) => {
        let alarmClockId = param['id'];
        console.log(alarmClockId);
        if (!alarmClockId){
          console.log("alarmClockId: no id");
          return
        }else{
          console.log("alarmClockId: get an id: " + alarmClockId);
          // we have an ID, load the object from it
          this.newAlarmClock = this.alarmClockService.getAlarmClockById(alarmClockId);
          console.log(this.newAlarmClock);
        }
      });
  }

  onSubmit() {
    // check if the id alrady exist
    let existingAlarmClock = this.alarmClockService.getAlarmClockById(this.newAlarmClock.id)
    if (existingAlarmClock){
      console.log("Alarm clock already exist, updating it with val" + existingAlarmClock);
      this.alarmClockService.updateAlarmClockById(this.newAlarmClock.id, this.newAlarmClock);
    }else{
      this.alarmClockService.addAlarmClock((this.newAlarmClock));
      this.newAlarmClock = new AlarmClock();
    }
    // return to web radio list
    this.router.navigate(["alarms"])
  }

  create_range(maxVal: number): number[]{
    var x=[];
    var i=0;
    while(x.push(i++)<=maxVal){};
    return x;
  }

}
