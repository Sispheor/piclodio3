import { Component, OnInit } from '@angular/core';
import { WebRadioService } from '../web-radio.service';
import { WebRadio } from '../web-radio';
import {Router, ActivatedRoute} from '@angular/router'
import {Subscription } from 'rxjs';

@Component({
  selector: 'app-web-radio-form',
  templateUrl: './web-radio-form.component.html',
  styleUrls: ['./web-radio-form.component.css']
})
export class WebRadioFormComponent implements OnInit {

  newWebradio: WebRadio = new WebRadio();
  private subscription: Subscription;

  constructor(
    private webRadioService: WebRadioService,
    private router: Router,
    private activatedRoute: ActivatedRoute
  ) { }

  ngOnInit() {
    // get the id in the URL
    this.subscription = this.activatedRoute.params.subscribe(
      (param: any) => {
        let webradioId = param['id'];
        console.log(webradioId);
        if (!webradioId){
          console.log("no id");
          return
        }else{
          console.log("get an id");
          // we have an ID, load the object from it
          this.newWebradio = this.webRadioService.getWebRadioById(webradioId);
          console.log(this.newWebradio);
        }
      });

  }

  onSubmit() {
    // check if the id alrady exist
    let existingWebRadio = this.webRadioService.getWebRadioById(this.newWebradio.id)
    if (existingWebRadio){
      this.webRadioService.updateWebRadioById(this.newWebradio.id, this.newWebradio)
    }else{
      this.webRadioService.addWebRadio(this.newWebradio)
      this.newWebradio = new WebRadio();
    }
    // return to web radio list
    this.router.navigate(["webradios"])
  }

}
