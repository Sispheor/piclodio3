import { Webradio } from './webradio';

export class Player {
    active: boolean;
    webradio: Webradio;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
