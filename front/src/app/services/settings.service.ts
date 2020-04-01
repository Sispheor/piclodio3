
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { globalVariables, BASE_API_URL } from '../../globalVariables';
import { map } from 'rxjs/operators';
import { Volume } from '../models/volume';
import { Backup } from '../models/backup';

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

    // POST /volume
    setVolume(volume: Volume): Observable<Volume> {
        let url = this._globalVariables.BASE_API_URL + "/volume/";
        return this.http.post<Volume>(url, volume).pipe(
            map(res => {
                return res
            })
        )
    }

    getBackup(): Observable<Backup[]> {
        let url = this._globalVariables.BASE_API_URL + "/backup/";
        return this.http.get<Backup[]>(url).pipe(
            map(res => {
                return res
            })
        )
    }

    postFile(fileToUpload: File): Observable<boolean> {
        let url = this._globalVariables.BASE_API_URL + "/backup/";
        const formData: FormData = new FormData();
        console.log(fileToUpload);
        formData.append('backup_file', fileToUpload, fileToUpload.name);
        return this.http.post(url, formData).pipe(
                map(() => {
                    return true;
                })
            )
    }

}
