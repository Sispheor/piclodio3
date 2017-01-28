import { Observable } from 'rxjs/Observable';
import { Http, Response } from '@angular/http';
import { Injectable } from '@angular/core';
import { WebRadio } from './web-radio';
import { WEBRADIOS } from '../mock-webradios';

@Injectable()
export class WebRadioService {
  // Placeholder for last id so we can simulate
  // automatic incrementing of id's
  lastId: number = 2;

  // Placeholder for webradio's. We get the mock for testing
  webradios: WebRadio[] = WEBRADIOS;

  baseUrl: string = "http://192.168.0.12:8000"

  constructor(private httpService: Http) { }

  // GET /webradios
  getAllWebRadios(): Observable<WebRadio[]> {
    //return this.webradios;
    var webRadios = this.httpService.get(this.baseUrl+"/webradio/")
                          // and calling .json() on the response to return data
                         .map((res:Response) => res.json())
  //  console.log(webRadios);

    return webRadios;
  }

  // GET /webradios/:id
  getWebRadioById(id: number):  Observable<WebRadio> {
    var returnedWebRadio = this.httpService.get(this.baseUrl+"/webradio/"+id)
                          // and calling .json() on the response to return data
                         .map((res:Response) => res.json())
    return returnedWebRadio;
  }

  // POST /webradios
  addWebRadio(webradio: WebRadio): WebRadioService {
    if (!webradio.id) {
      webradio.id = ++this.lastId;
    }
    this.webradios.push(webradio);
    return this;
  }

  // DELETE /webradios/:id
  deleteWebRadioById(id: number): Observable<any> { 
    // TODO : fix this shit. The method is called but not the backend. FU angular.
    console.log("call delete service, delete webradio id " + id);
    
    return this.httpService.delete(this.baseUrl+"/webradio/"+id)                          
                         .map((res:Response) => res.json());
  }

  //  PUT /todos/:id
  updateWebRadioById(id: number, values: Object = {}): Observable<WebRadio>  {
    let webradio = this.getWebRadioById(id);
    if (!webradio) {
      return null;
    }
    Object.assign(webradio, values);
    return webradio;
  }


}
