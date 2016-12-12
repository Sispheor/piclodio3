import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule }   from '@angular/router';

import { AppComponent } from './app.component';
import { WebRadiosComponent } from './web-radios/web-radios.component';
import { HomepageComponent } from './homepage/homepage.component';

import { WebRadioService } from './web-radios/web-radio.service';
import { AlarmClockComponent } from './alarm-clock/alarm-clock.component';

@NgModule({
  declarations: [
    AppComponent,
    WebRadiosComponent,
    HomepageComponent,
    AlarmClockComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
      {
        path: 'homepage',
        component: HomepageComponent
      },
      {
        path: 'webradios',
        component: WebRadiosComponent
      },
      {
        path: 'alarms',
        component: AlarmClockComponent
      }
    ])
  ],
  providers: [WebRadioService],
  bootstrap: [AppComponent]
})
export class AppModule { }
