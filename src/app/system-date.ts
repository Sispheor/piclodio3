export class SystemDate {
    hour: number;
    minute: number;
    second: number;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }

}
