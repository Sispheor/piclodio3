import {DayOfWeek} from "./day-of-week";
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-day-of-week',
  templateUrl: './day-of-week.component.html',
  styleUrls: ['./day-of-week.component.css']
})
export class DayOfWeekComponent {

  @Input()
  dayofweek: DayOfWeek;

  constructor() { }

  ngOnInit() {
  }

}
