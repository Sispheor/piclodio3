import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription, interval, Observable } from 'rxjs';
import { ClockService } from '../services/clock.service';

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

  constructor(private clockService: ClockService) { }

  ngOnInit() {
    // get the backend server time and date
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


  ngOnDestroy() {
    this.systemDateSubscribption.unsubscribe();
    if (this.clockIncrementSubscription) {
      this.clockIncrementSubscription.unsubscribe();
    }

  }

}
