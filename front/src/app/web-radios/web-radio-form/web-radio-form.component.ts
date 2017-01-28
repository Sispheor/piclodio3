import { NoSwitchCaseFallThroughWalker } from 'tslint/lib/rules/noSwitchCaseFallThroughRule';
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
  existingWebRadio: Boolean = true;
  private subscription: Subscription;

  constructor(
    private webRadioService: WebRadioService,
    private router: Router,
    private activatedRoute: ActivatedRoute
  ) {}

  ngOnInit() {
    // get the id in the URL
    this.subscription = this.activatedRoute.params.subscribe(
      (param: any) => {
        let webradioId = param['id'];
        console.log(webradioId);
        if (!webradioId) {
          console.log("no id");
          this.existingWebRadio = false;
          return
        } else {
          console.log("get an id");
          // we have an ID, load the object from it
          this.webRadioService.getWebRadioById(webradioId).subscribe(newWebradio => this.newWebradio = newWebradio,
            error => console.error('Error: ' + error),
            () => console.log('Completed!'));
          console.log(this.newWebradio);
        }
      });

  }

  onSubmit() {
    console.log("web-radio form: onSubmit clicked")
    // check if the id alrady exist    
    if (this.existingWebRadio) {
      // let webRadioToUpdate = this.webRadioService.getWebRadioById(this.newWebradio.id).toPromise()      
      console.log("web-radio form: webradio with id "+ this.newWebradio.id +" already exist. Call update service");
      this.webRadioService.updateWebRadioById(this.newWebradio.id, this.newWebradio).subscribe(
        success => {          
          this.router.navigate(["webradios"]);
        },
        error => console.log("Error "+ error)
      );
    } else {
      console.log("Create new web radio");
      this.webRadioService.addWebRadio(this.newWebradio).subscribe(
        success => {          
          this.router.navigate(["webradios"]);
        },
        error => console.log("Error "+ error)
      );
      
    }
    
  }

}
