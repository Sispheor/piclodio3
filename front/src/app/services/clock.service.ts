import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { globalVariables, BASE_API_URL } from '../../globalVariables';

@Injectable({
  providedIn: 'root'
})
export class ClockService {


  constructor(private _globalVariables: globalVariables, private http: HttpClient) { }

  // GET /alarmclocks
  getSystemDate() {
    return this.http.get(this._globalVariables.BASE_API_URL + "/clock/");
  }

}
