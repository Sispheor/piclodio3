export class DayOfWeek {
  monday: boolean  = false;
  tuesday: boolean  = false;
  wednesday: boolean  = false;
  thursday: boolean  = false;
  friday: boolean  = false;
  saturday: boolean  = false;
  sunday: boolean  = false;

  constructor(values: Object = {}) {
      Object.assign(this, values);
  }
}
