
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { globalVariables, BASE_API_URL } from '../../globalVariables';
import { map } from 'rxjs/operators';
import { Volume } from '../models/volume';

@Injectable({
    providedIn: 'root'
})
export class SettingsService {


    constructor(private _globalVariables: globalVariables, private http: HttpClient) { }

    // GET /volume
    getVolume(): Observable<Volume> {
        let url = this._globalVariables.BASE_API_URL + "/volume/";
        return this.http.get<Volume>(url).pipe(
            map(res => {
                return res
            })
        )
    }

    // GET /volume
    setVolume(volume: Volume): Observable<Volume> {
        let url = this._globalVariables.BASE_API_URL + "/volume/";
        return this.http.post<Volume>(url, volume).pipe(
            map(res => {
                return res
            })
        )
    }

}
