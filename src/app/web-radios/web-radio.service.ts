import { Injectable } from '@angular/core';
import { WebRadio } from './web-radio';
import { WEBRADIOS } from '../mock-webradios';

@Injectable()
export class WebRadioService {
  // Placeholder for last id so we can simulate
  // automatic incrementing of id's
  lastId: number = 0;

  // Placeholder for webradio's. We get the mock for testing
  webradios: WebRadio[] = WEBRADIOS;

  constructor() { }
  // Simulate GET /webradios
  getAllWebRadios(): WebRadio[] {
    return this.webradios;
  }

  // Simulate POST /webradios
  addWebRadio(webradio: WebRadio): WebRadioService {
    if (!webradio.id) {
      webradio.id = ++this.lastId;
    }
    this.webradios.push(webradio);
    return this;
  }  


}
