export class Player {
    status: string = "off";    

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
