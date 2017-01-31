import { Backup } from './backup';
import { Volume } from './volume';
import { GlobalVariable } from './../globals';
import { Http, Response, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';

@Injectable()
export class OptionService {

  baseUrl: string = GlobalVariable.BASE_API_URL;

  constructor(private httpService: Http) { }

  getVolume(): Observable <Volume> {
    var volume = this.httpService.get(this.baseUrl + "/volume/")
      .map((res: Response) => res.json())
    return volume;
  }


  setVolume(volume: Volume): Observable < Volume > {
    let body = JSON.stringify(volume); // Stringify payload
    let headers = new Headers({
      'Content-Type': 'application/json'
    });
    var newVolume = this.httpService.post(this.baseUrl + "/volume/", body, {
        headers: headers
      })
      .map((res: Response) => res.json())
    return newVolume;
  }

  getBackup(): Observable <Backup[]> {
    var backup = this.httpService.get(this.baseUrl + "/backup/")
      .map((res: Response) => res.json())
    return backup;
  }

}
