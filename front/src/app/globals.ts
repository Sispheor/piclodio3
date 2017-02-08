import {DOCUMENT} from '@angular/platform-browser';

// we supose that the backend is on the same server. if not, replace this export by a hard coded ip
export const hostname = document.location.hostname
export const BASE_API_URL = "http://"+hostname+":8000"

export const GlobalVariable = Object.freeze({
    BASE_API_URL: BASE_API_URL,
    //... more of your variables
});