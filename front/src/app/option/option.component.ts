import { Volume } from './volume';
import { OptionService } from './option.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-option',
  templateUrl: './option.component.html',
  styleUrls: ['./option.component.css']
})
export class OptionComponent implements OnInit {

  currentVolume: Volume;
  volumeLoaded: boolean = false;

  constructor(private optionService: OptionService) { }

  ngOnInit() {
    // get the current volume
    this.refreshVolume();
  }

  refreshVolume(){
    this.optionService.getVolume().subscribe(this.setVolume.bind(this));
  }

  setVolume(volume: Volume){
    this.currentVolume = volume;
    this.volumeLoaded = true;
  }

  reduceVolume(){
    let newVolumeLevel = this.currentVolume.volume;
    newVolumeLevel = newVolumeLevel - 10 ;
    if (newVolumeLevel < 0){
      newVolumeLevel = 0;
    }
    this.currentVolume.volume = newVolumeLevel
    this.optionService.setVolume(this.currentVolume).subscribe(
      success => {
          this.refreshVolume();
        },
        error => console.log("Error "+ error)
      );
  }

  increaseVolume(){
    let newVolumeLevel = this.currentVolume.volume;
    newVolumeLevel = newVolumeLevel + 10 ;
    if (newVolumeLevel > 100){
      newVolumeLevel = 100;
    }
    this.currentVolume.volume = newVolumeLevel
    this.optionService.setVolume(this.currentVolume).subscribe(
      success => {
          this.refreshVolume();
        },
        error => console.log("Error "+ error)
      );
  }

}
