import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ClockService {

  baseUrl: string = "http://192.168.0.22:8000/api"

  constructor(private http: HttpClient) { }

  // GET /alarmclocks
  getSystemDate() {
    return this.http.get(this.baseUrl + "/clock/");
  }

}
