
export class Player {
    status: string = "off";
    webradio: number;   

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
