import { WebRadio } from '../web-radios/web-radio';

export class AlarmClock {
    id: number;
    name: string = '';
    hour: number;
    minute: number;    
    is_active: boolean = false;
    webradio: WebRadio;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
