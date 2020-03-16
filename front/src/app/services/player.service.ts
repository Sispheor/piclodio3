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
    url = this._globalVariables.BASE_API_URL + "/player/";

    constructor(private _globalVariables: globalVariables, private http: HttpClient) { }

    getPlayerStatus(): Observable<Player> {
        
        return this.http.get<Player>(this.url).pipe(
            map(res => {
                return res
            })
        )  
    }

    setPlayerStatus(player: Player): Observable<Player> {
        let body = {
            "active": player.active,
            "webradio": player.webradio.id
        }
        return this.http.post<Player>(this.url, body).pipe(
            map(res => {
                console.log(res);
                return res
            })
        )  
    }

}
