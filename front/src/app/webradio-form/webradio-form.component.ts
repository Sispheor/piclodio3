import { Component, OnInit } from '@angular/core';
import { Webradio } from '../models/webradio';
import { WebRadioService } from '../services/webradio.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-webradio-form',
  templateUrl: './webradio-form.component.html',
  styleUrls: ['./webradio-form.component.scss']
})
export class WebradioFormComponent implements OnInit {

  newWebradio: Webradio = new Webradio();

  constructor(private webRadioService: WebRadioService,
              private router: Router) { }

  ngOnInit(): void { }

  onSubmit() {
    console.log("Create new web radio");
    console.log(this.newWebradio);
    this.webRadioService.addWebRadio(this.newWebradio).subscribe(
      success => {
        this.router.navigate(["webradios"]);
      },
      error => console.log("Error " + error)
    )
  }

}
