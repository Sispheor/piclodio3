import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription, interval, Observable } from 'rxjs';
import { ClockService } from '../services/clock.service';
import { AlarmsService } from '../services/alarms.service';
import { Alarm } from '../models/alarm';
import { WebRadioService } from '../services/webradio.service';
import { Webradio } from '../models/webradio';
import { PlayerService } from '../services/player.service';
import { Player } from '../models/player';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit, OnDestroy {
  clock: Date;
  clockString: string;
  systemDateSubscribption: Subscription;
  clockIncrementSubscription: Subscription;
  active_alarms: Alarm[];
  all_webradios: Webradio[];
  active_webradios: Webradio[];
  playerLoaded: boolean = false;
  player: Player;

  constructor(private clockService: ClockService,
              private alarmService: AlarmsService,
              private webRadioService: WebRadioService,
              private playerService: PlayerService) { }

  ngOnInit() {
    // get the backend server time and date
    this.getBackendDate();
    // get list of alarm
    this.alarmService.getAlarms().subscribe(this.setActiveAlarmClocks.bind(this));
    // get the active web radio
    this.webRadioService.getAllWebRadios().subscribe(this.filterDefaultWebRadio.bind(this));
    // get the player status
    this.playerService.getPlayerStatus().subscribe(this.setPlayerStatus.bind(this));
 
  }

  getBackendDate() {
    this.systemDateSubscribption = this.clockService.getSystemDate().subscribe(
      (value) => {
        console.log("Received date from backend server: ");
        console.log(value);
        this.setIncrementDataObservable(value)
      },
      (error) => {
        console.log('Uh-oh, an error occurred! : ' + error);
      },
      () => {
        console.log("Observable 'getSystemDate' complete");
      }
    );
  }

  setIncrementDataObservable(dataObject: Object){

    this.clock = new Date(dataObject["clock"])
    const counter = interval(1000);
    this.clockIncrementSubscription = counter.subscribe(
      (value) => {
        this.clock.setSeconds(this.clock.getSeconds() + 1)
        this.clockString = this.clock.toString();
      },
      (error) => {
        console.log('Uh-oh, an error occurred! : ' + error);
      },
      () => {
        console.log('Observable complete!');
      }   
    );
  }

  setActiveAlarmClocks(alarms: Alarm[]){
    this.active_alarms = alarms.filter(
      alarm => alarm.enabled === true
    )
    console.log("Alarms:")
    console.log(alarms)
  }


  ngOnDestroy() {
    this.systemDateSubscribption.unsubscribe();
    if (this.clockIncrementSubscription) {
      this.clockIncrementSubscription.unsubscribe();
    }

  }

  /**
   * Filter the received list of webradios to keep only the active one (is_default)
   */
  filterDefaultWebRadio(webradios: Webradio[]) {
    this.all_webradios = webradios;
    console.log("Web Radios:")
    console.log(webradios);
    this.active_webradios = this.all_webradios.filter(
      webradio => webradio.is_default === true
    )
  }

  setPlayerStatus(player: Player) {
    console.log("Player: ");
    console.log(player);
    this.player = player;
    this.playerLoaded = true;
  }

}
