import { Component, OnInit } from '@angular/core';
import { Alarm } from '../models/alarm';
import { WebRadioService } from '../services/webradio.service';
import { Webradio } from '../models/webradio';
import { FormGroup, FormControl, ValidatorFn, Validators  } from '@angular/forms';
import { threadId } from 'worker_threads';
import { AlarmsService } from '../services/alarms.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-alarm-form',
  templateUrl: './alarm-form.component.html',
  styleUrls: ['./alarm-form.component.scss']
})
export class AlarmFormComponent implements OnInit {

  webradios: Webradio[];
  newAlarm: Alarm = new Alarm();
  default_time = { hour: 7, minute: 0 };
  dayOfWeek = [
    { name: 'order 1' },
    { name: 'order 2' },
    { name: 'order 3' },
    { name: 'order 4' }
  ];

  form;

  constructor(private webRadioService: WebRadioService,
              private alarmService: AlarmsService,
              private router: Router) { }

  ngOnInit(): void {
    this.newAlarm.auto_stop_minutes = 0;

    // get the active web radio
    this.webRadioService.getAllWebRadios().subscribe(this.setWebRadio.bind(this));

    this.createEmptyForm()

  }

  createEmptyForm() {
    this.form = new FormGroup({
      name: new FormControl('', [Validators.required]),
      myCheckboxGroup: new FormGroup({
        monday: new FormControl(false),
        tuesday: new FormControl(false),
        wednesday: new FormControl(false),
        thursday: new FormControl(false),
        friday: new FormControl(false),
        saturday: new FormControl(false),
        sunday: new FormControl(false),
      }, requireCheckboxesToBeCheckedValidator()),
      time: new FormControl(this.default_time, [Validators.required]),
      auto_stop_minutes: new FormControl(0, [Validators.required]),
      webradio: new FormControl('', [Validators.required])
    });

  }

  setWebRadio(webradios: Webradio[]) {
    this.webradios = webradios;
  }

  onSubmit(){
    console.warn(this.form.value);
    this.newAlarm.name = this.form.value.name;
    this.newAlarm.monday = this.form.value.myCheckboxGroup.monday;
    this.newAlarm.tuesday = this.form.value.myCheckboxGroup.tuesday;
    this.newAlarm.wednesday = this.form.value.myCheckboxGroup.wednesday;
    this.newAlarm.thursday = this.form.value.myCheckboxGroup.thursday;
    this.newAlarm.friday = this.form.value.myCheckboxGroup.friday;
    this.newAlarm.saturday = this.form.value.myCheckboxGroup.saturday;
    this.newAlarm.sunday = this.form.value.myCheckboxGroup.sunday;
    this.newAlarm.hour = this.form.value.time.hour;
    this.newAlarm.minute = this.form.value.time.minute;
    this.newAlarm.auto_stop_minutes = this.form.value.auto_stop_minutes;
    this.newAlarm.webradio = this.form.value.webradio;
    this.alarmService.createAlarm(this.newAlarm).subscribe(
      success => {
        this.router.navigate(["alarms"]);
      },
      error => {
        console.log("Error creating new alarm");
        console.log(error);
      }
    )
  }


}

export function requireCheckboxesToBeCheckedValidator(minRequired = 1): ValidatorFn {
  return function validate(formGroup: FormGroup) {
    let checked = 0;

    Object.keys(formGroup.controls).forEach(key => {
      const control = formGroup.controls[key];

      if (control.value === true) {
        checked++;
      }
    });

    if (checked < minRequired) {
      return {
        requireCheckboxesToBeChecked: true,
      };
    }

    return null;
  };


}
