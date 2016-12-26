import {WebRadio} from "./web-radios/web-radio";
import {AlarmClock} from "./alarm-clock/alarm-clock";
import { WEBRADIOS } from './mock-webradios';

var webradios = WEBRADIOS
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
    webradio: webradios[1]
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
    webradio: webradios[0]
  }

];
