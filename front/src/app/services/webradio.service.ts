
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

    // POST /webradios
    addWebRadio(webradio: Webradio): Observable<Webradio> {
        let url = this._globalVariables.BASE_API_URL + "/webradios/";

        return this.http.post<Webradio>(url, webradio).pipe(
            map(res => {
                console.log(res);
                return res
            })
        )
    }

    // DELETE /webradios/:id
    deleteWebradio(webradio: Webradio): Observable<any> {
        let url = this._globalVariables.BASE_API_URL + "/webradios/"+ webradio.id;

        return this.http.delete<Webradio>(url).pipe(
            map(res => {
                console.log(res);
                return res
            })
        )
    }
}

export interface GetWebRadiosResponse extends BaseResponse {
    results: Array<Webradio>;
}