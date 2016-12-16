import {DayOfWeek} from "./day-of-week";
import { WebRadio } from '../web-radios/web-radio';

export class AlarmClock {
    id: number;
    name: string = '';
    dayofweek: DayOfWeek;
    hour: number;
    minute: number;
    is_active: boolean = false;
    webradio: WebRadio;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
