import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],

})
export class AppComponent {
  public isCollapsed: boolean = true;

  public collapsed(event:any):void {
    console.log("collapsed called");
  }

  public expanded(event:any):void {
    console.log("expanded called");
  }
}

