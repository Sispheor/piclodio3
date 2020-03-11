import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription, interval, Observable } from 'rxjs';
import { ClockService } from '../services/clock.service';
import { AlarmsService } from '../services/alarms.service';
import { Alarm } from '../models/alarm';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit, OnDestroy {
  clock: Date;
  clockString: string;
  systemDateSubscribption: Subscription;
  clockIncrementSubscription: Subscription;
  active_alarms: Alarm[];

  constructor(private clockService: ClockService,
              private alarmService: AlarmsService) { }

  ngOnInit() {
    // get the backend server time and date
    this.getBackendDate();
    // get list of alarm
    this.alarmService.getAlarms().subscribe(this.setActiveAlarmClocks.bind(this));
 
  }

  getBackendDate() {
    this.systemDateSubscribption = this.clockService.getSystemDate().subscribe(
      (value) => {
        console.log("Received date from backend server: ");
        console.log(value);
        this.setIncrementDataObservable(value)
      },
      (error) => {
        console.log('Uh-oh, an error occurred! : ' + error);
      },
      () => {
        console.log("Observable 'getSystemDate' complete");
      }
    );
  }

  setIncrementDataObservable(dataObject: Object){

    this.clock = new Date(dataObject["clock"])
    const counter = interval(1000);
    this.clockIncrementSubscription = counter.subscribe(
      (value) => {
        this.clock.setSeconds(this.clock.getSeconds() + 1)
        this.clockString = this.clock.toString();
      },
      (error) => {
        console.log('Uh-oh, an error occurred! : ' + error);
      },
      () => {
        console.log('Observable complete!');
      }   
    );
  }

  setActiveAlarmClocks(alarms: Alarm[]){
    this.active_alarms = alarms.filter(
      alarm => alarm.enabled === true
    )
    console.log(alarms)
  }


  ngOnDestroy() {
    this.systemDateSubscribption.unsubscribe();
    if (this.clockIncrementSubscription) {
      this.clockIncrementSubscription.unsubscribe();
    }

  }

}
