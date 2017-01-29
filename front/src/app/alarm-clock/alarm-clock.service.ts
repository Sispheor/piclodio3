import { GlobalVariable } from './../globals';
import { Http, Response, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import {AlarmClock} from "./alarm-clock";
import { Injectable } from '@angular/core';

@Injectable()
export class AlarmClockService {
  
  baseUrl: string = GlobalVariable.BASE_API_URL;

  constructor(private httpService: Http) { }

  // GET /alarmclocks
  getAllAlarmClocks(): Observable <AlarmClock[]> {
    var alarmClocks = this.httpService.get(this.baseUrl + "/alarms/")      
      .map((res: Response) => res.json())    
    return alarmClocks;
  }

  // DELETE /alarms/:id
  deleteAlarmClockById(id: number): Observable < any > {
    console.log("call delete service, delete alarm id " + id);
    return this.httpService.delete(this.baseUrl + "/alarms/" + id)
      .map((res: Response) => res.json());
  }

  // POST /alarms/new
  addAlarmClock(alarmClock: AlarmClock): Observable <AlarmClock> {
    let body = JSON.stringify(alarmClock); // Stringify payload
    let headers = new Headers({
      'Content-Type': 'application/json'
    });
    var returnedAlarmClock = this.httpService.post(this.baseUrl + "/alarms/", body, {
        headers: headers
      })
      .map((res: Response) => res.json())
    return returnedAlarmClock;
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
