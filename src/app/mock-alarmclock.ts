import {AlarmClock} from "./alarm-clock/alarm-clock";

// fake list of alarm-clock
export const ALARMCLOCK: AlarmClock[] = [
  { id: 1,
    name: "work",
    dayofweek: {
      "monday": true,
      "tuesday": true,
      "wednesday": true,
      "thursday": true,
      "friday": true,
      "saturday": false,
      "sunday": false
    },
    hour: 7,
    minute: 30,
    is_active: true,
    webradio: {
      id: 1,
      name: 'webradio1',
      url: "http://webradio.com",
      is_active: true
    }
  },
  { id: 2,
    name: "week-end",
    dayofweek: {
      "monday": false,
      "tuesday": false,
      "wednesday": false,
      "thursday": false,
      "friday": false,
      "saturday": true,
      "sunday": true
    },
    hour: 10,
    minute: 30,
    is_active: false,
    webradio: {
      id: 2,
      name: 'webradio2',
      url: "http://webradio2.com",
      is_active: false
    }
  }

];
