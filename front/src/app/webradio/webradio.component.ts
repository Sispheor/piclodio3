import { Component, OnInit } from '@angular/core';
import { Webradio } from '../models/webradio';
import { WebRadioService } from '../services/webradio.service';
import { Player } from '../models/player';
import { PlayerService } from '../services/player.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-webradio',
  templateUrl: './webradio.component.html',
  styleUrls: ['./webradio.component.scss']
})
export class WebradioComponent implements OnInit {

  webradios: Webradio[] = [];

  constructor(private router: Router,
              private webRadioService: WebRadioService,
              private playerService: PlayerService) { }

  ngOnInit(): void {
    this.webRadioService.getAllWebRadios().subscribe(this.setWebRadios.bind(this));
  }

  setWebRadios(webradios: Webradio[]){
    this.webradios = webradios;
  }

  playWebRadio(webradio: Webradio) {
    console.log("Play web radio id " + webradio.id);
    let player = new Player();
    player.active = true;
    player.webradio = webradio;
    this.playerService.setPlayerStatus(player).subscribe(
      (value) => {
        this.router.navigate(["homepage"]);
      },
      (error) => {
        console.log("Error " + error)
      },
      () => {
        console.log("Observable 'getSystemDate' complete");
      }
    );

  }

}
