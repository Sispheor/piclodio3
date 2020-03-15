
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { globalVariables, BASE_API_URL } from '../../globalVariables';
import { map } from 'rxjs/operators';
import { Webradio } from '../models/webradio';
import { BaseResponse } from './baseResponse';

@Injectable({
    providedIn: 'root'
})
export class WebRadioService {


    constructor(private _globalVariables: globalVariables, private http: HttpClient) { }

    // GET /webradios
    getAllWebRadios(): Observable<Webradio[]> {
        let url = this._globalVariables.BASE_API_URL + "/webradios/";
        return this.http.get<GetWebRadiosResponse>(url).pipe(
            map(res => {
                return res.results
            })
        )        
    }
}

export interface GetWebRadiosResponse extends BaseResponse {
    results: Array<Webradio>;
}