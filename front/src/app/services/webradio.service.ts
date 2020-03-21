
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
        return this.http.get<GetListWebRadiosResponse>(url).pipe(
            map(res => {
                return res.results
            })
        )
    }

    // GET /webradios/:id
    getWebRadioById(id: number): Observable<Webradio> {
        let url = this._globalVariables.BASE_API_URL + "/webradios/" + id;
        return this.http.get<Webradio>(url).pipe(
                map(res => {
                    console.log(res);
                    return res
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

    //  PUT /webradios/:id
    updateWebradio(webradio: Webradio): Observable<Webradio> {
        let url = this._globalVariables.BASE_API_URL + "/webradios/" + webradio.id + "/";
        return this.http.put<Webradio>(url, webradio).pipe(
            map(res => {
                console.log(res);
                return res
            })
        )
    }
}

export interface GetListWebRadiosResponse extends BaseResponse {
    results: Array<Webradio>;
}