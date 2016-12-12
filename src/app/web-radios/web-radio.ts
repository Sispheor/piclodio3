export class WebRadio {
    id: number;
    name: string = '';
    url: string = '';
    is_active: boolean = false;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
