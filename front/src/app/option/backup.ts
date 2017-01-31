export class Backup {
    id: number;
    backup_file: string;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }

}
