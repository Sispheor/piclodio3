import { GlobalVariable } from './../globals';
import { Http, Response, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
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

  baseUrl: string = GlobalVariable.BASE_API_URL;

  constructor(private httpService: Http) { }

  // GET /alarmclocks
  getAllAlarmClocks(): Observable <AlarmClock[]> {
    var alarmClocks = this.httpService.get(this.baseUrl + "/alarms/")      
      .map((res: Response) => res.json())    
    return alarmClocks;
  }

  // DELETE /alarms/:id
  deleteAlarmClockById(id: number): AlarmClockService {
    this.alarmclocks = this.alarmclocks
      .filter(alarmclock => alarmclock.id !== id);
    return this;
  }

  // POST /alarms/new
  addAlarmClock(alarmClock: AlarmClock): AlarmClockService {
    if (!alarmClock.id) {
      alarmClock.id = ++this.lastId;
    }
    this.alarmclocks.push(alarmClock);
    return this;
  }

  // GET /alarms/:id
  getAlarmClockById(id: number): Observable <AlarmClock> {
    var returnedAlarmClock = this.httpService.get(this.baseUrl + "/alarms/" + id)      
      .map((res: Response) => res.json())
    return returnedAlarmClock;
  }

  updateAlarmClockById(id: number, values: Object = {}): Observable <AlarmClock> {        
    let body = JSON.stringify(values); // Stringify payload
    let headers = new Headers({
      'Content-Type': 'application/json'
    });
    var returnedAlarmClock = this.httpService.put(this.baseUrl + "/alarms/" + id, body, {
        headers: headers
      })
      .map((res: Response) => res.json())
    return returnedAlarmClock;
  }


}
