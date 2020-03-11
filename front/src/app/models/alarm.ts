import { Webradio } from './webradio';
export class Alarm {
    id: number;
    name: string = '';
    monday: boolean = false;
    tuesday: boolean = false;
    wednesday: boolean = false;
    thursday: boolean = false;
    friday: boolean = false;
    saturday: boolean = false;
    sunday: boolean = false;
    hour: number;
    minute: number;
    auto_stop_minutes: number;
    enabled: boolean = false;
    webradio: Webradio;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
