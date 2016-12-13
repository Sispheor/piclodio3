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

  constructor() { }
  
  // GET /webradios
  getAllWebRadios(): WebRadio[] {
    return this.webradios;
  }

  // GET /webradios/:id
  getWebRadioById(id: number): WebRadio {    
    let returnedWebRadio = this.webradios
      .find(x => Number(x.id) === Number(id));     
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
  deleteWebRadioById(id: number): WebRadioService {
    this.webradios = this.webradios
      .filter(webradio => webradio.id !== id);
    return this;
  }


}
