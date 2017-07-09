import { GlobalVariable } from './../globals';
import { Observable } from 'rxjs/Observable';
import * as url from 'url';
import { Http, Response } from '@angular/http';
import { Injectable } from '@angular/core';


@Injectable()
export class SystemDateService {

    baseUrl: string = GlobalVariable.BASE_API_URL;

    constructor(private httpService: Http) {}

    // GET /alarmclocks
    getSystemDate(): Observable < Date > {
        var datejsonObservable = this.httpService.get(this.baseUrl + "/systemdate/");
        return this.dateJson(datejsonObservable);
    }

    dateJson(datejsonObservable: Observable < Response > ): Observable < Date > {
        var jsonDateString: Observable < string > = datejsonObservable.map((response: Response) => response.json());
        return jsonDateString.map((date: string) => new Date(date));
    }
}
