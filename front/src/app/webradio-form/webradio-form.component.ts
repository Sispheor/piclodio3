import { Component, OnInit } from '@angular/core';
import { Webradio } from '../models/webradio';
import { WebRadioService } from '../services/webradio.service';
import { Router, ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { ToastService } from '../services/toast.service';

@Component({
  selector: 'app-webradio-form',
  templateUrl: './webradio-form.component.html',
  styleUrls: ['./webradio-form.component.scss']
})
export class WebradioFormComponent implements OnInit {

  newWebradio: Webradio = new Webradio();
  existingWebRadio: Boolean = true;
  private routeSub: Subscription;

  constructor(private webRadioService: WebRadioService,
              private router: Router,
              private activatedRoute: ActivatedRoute,
              public toastService: ToastService) { }

  ngOnInit(): void {
    this.routeSub = this.activatedRoute.params.subscribe(params => {
      let webradioId = params['id'];
      if (!webradioId) {
        console.log("no webradio id");
        this.existingWebRadio = false;
        return
      } else {
        this.webRadioService.getWebRadioById(webradioId).subscribe(newWebradio => this.newWebradio = newWebradio,
          error => console.error('Error: ' + error),
          () => console.log('Completed!'));
        console.log(this.newWebradio);
      }
    });
  }

  onSubmit() {
    if (this.existingWebRadio){
      console.log("Update existing web radio");
      this.webRadioService.updateWebradio(this.newWebradio).subscribe(
        success => {
          this.toastService.show('Web radio updated', { classname: 'bg-info text-light', delay: 5000 });
          this.router.navigate(["webradios"]);
        },
        error => {
          console.log("Error " + error);
          this.toastService.show('Error', { classname: 'bg-danger text-light', delay: 5000 });
        }
      );

    }else{
      console.log("Create new web radio");
      console.log(this.newWebradio);
      this.webRadioService.addWebRadio(this.newWebradio).subscribe(
        success => {
          this.toastService.show('Web radio created', { classname: 'bg-info text-light', delay: 5000 });
          this.router.navigate(["webradios"]);
        },
        error => {
          console.log("Error " + error);
          this.toastService.show('Error', { classname: 'bg-danger text-light', delay: 5000 });
        }
      )
    }
  }

  ngOnDestroy() {
    this.routeSub.unsubscribe();
  }

}
