import {AlarmClock} from "./alarm-clock";
import { Injectable } from '@angular/core';
import { ALARMCLOCK } from '../mock-alarmclock';


@Injectable()
export class AlarmClockService {
  // Placeholder for last id so we can simulate
  // automatic incrementing of id's
  lastId: number = 2;

  // Placeholder for webradio's. We get the mock for testing
  alarmclocks: AlarmClock[] = ALARMCLOCK;


  constructor() { }

  // GET /alarmclocks
  getAllAlarmClocks(): AlarmClock[] {
    return this.alarmclocks;
  }

  // DELETE /alarms/:id
  deleteAlarmClockById(id: number): AlarmClockService {
    this.alarmclocks = this.alarmclocks
      .filter(alarmclock => alarmclock.id !== id);
    return this;
  }


}
