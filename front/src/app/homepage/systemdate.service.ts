import { Observable } from 'rxjs/Observable';
import { Console } from '@angular/compiler-cli/src/private_import_core';
import * as url from 'url';
import { Http, Response } from '@angular/http';
import { Injectable } from '@angular/core';


@Injectable()
export class SystemDateService {    

    constructor(private httpService: Http) { }

    // GET /alarmclocks
    getSystemDate(): Observable<Date> {
        
        var datejsonObservable = this.httpService.get("http://10.33.101.127:8000/systemdate/");

        return this.dateJson(datejsonObservable)
        
    }

    dateJson(datejsonObservable: Observable<Response>): Observable<Date>{
        var jsonDateString: Observable<string> = datejsonObservable.map((response: Response) => response.json());
        return jsonDateString.map((date:string) => new Date(date));
    }

}


//