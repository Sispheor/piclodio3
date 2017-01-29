import { GlobalVariable } from './../globals';
import { Observable } from 'rxjs/Observable';
import { Headers, Http, Response } from '@angular/http';
import { Injectable } from '@angular/core';
import { WebRadio } from './web-radio';

@Injectable()
export class WebRadioService {
 
  baseUrl: string = GlobalVariable.BASE_API_URL;

  constructor(private httpService: Http) {}

  // GET /webradios
  getAllWebRadios(): Observable < WebRadio[] > {    
    var webRadios = this.httpService.get(this.baseUrl + "/webradio/")      
      .map((res: Response) => res.json())    
    return webRadios;
  }

  // GET /webradios/:id
  getWebRadioById(id: number): Observable < WebRadio > {
    var returnedWebRadio = this.httpService.get(this.baseUrl + "/webradio/" + id)      
      .map((res: Response) => res.json())
    return returnedWebRadio;
  }

  // POST /webradios
  addWebRadio(webradio: WebRadio): Observable < WebRadio > {
    let body = JSON.stringify(webradio); // Stringify payload
    let headers = new Headers({
      'Content-Type': 'application/json'
    });
    var returnedWebRadio = this.httpService.post(this.baseUrl + "/webradio/", body, {
        headers: headers
      })
      .map((res: Response) => res.json())
    return returnedWebRadio;
  }

  // DELETE /webradios/:id
  deleteWebRadioById(id: number): Observable < any > {
    console.log("call delete service, delete webradio id " + id);
    return this.httpService.delete(this.baseUrl + "/webradio/" + id)
      .map((res: Response) => res.json());
  }

  //  PUT /todos/:id
  updateWebRadioById(id: number, values: Object = {}): Observable < WebRadio > {

    let body = JSON.stringify(values); // Stringify payload
    let headers = new Headers({
      'Content-Type': 'application/json'
    });
    var returnedWebRadio = this.httpService.put(this.baseUrl + "/webradio/" + id, body, {
        headers: headers
      })
      .map((res: Response) => res.json())
    return returnedWebRadio;
  }
}
