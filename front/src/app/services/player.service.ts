import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { globalVariables, BASE_API_URL } from '../../globalVariables';
import { Player } from '../models/player';
import { map } from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
})
export class PlayerService {


    constructor(private _globalVariables: globalVariables, private http: HttpClient) { }

    getPlayerStatus(): Observable<Player> {
        let url = this._globalVariables.BASE_API_URL + "/player/";
        return this.http.get<Player>(url).pipe(
            map(res => {
                return res
            })
        )  
    }

}
