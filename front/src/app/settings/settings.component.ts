import { Component, OnInit } from '@angular/core';
import { SettingsService } from '../services/settings.service';
import { Volume } from '../models/volume';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.scss']
})
export class SettingsComponent implements OnInit {

  volumeLoaded = false;
  volume: Volume = { volume: "0"}

  constructor(private settingsService: SettingsService) { }

  ngOnInit(): void {
    this.refreshVolume()
  }

  refreshVolume() {
    this.settingsService.getVolume().subscribe(this.setVolume.bind(this));
  }

  setVolume(volume: Volume) {
    this.volume = volume;
    this.volumeLoaded = true;
  }

  volumeDown() {
    if (this.volume.volume == "0") {
      console.log("volume already at the minimum value")
    }else{
      let newVolumeLevel = +this.volume.volume;
      newVolumeLevel = newVolumeLevel - 5;
      if (newVolumeLevel < 0) {
        newVolumeLevel = 0;
      }
      let targetVolume: Volume = { volume: newVolumeLevel.toString()}
      this.settingsService.setVolume(targetVolume).subscribe(
        success => {
          this.refreshVolume();
        },
        error => console.log("Error " + error)
      );
    }
  }

  volumeUp() {
    if (this.volume.volume == "100") {
      console.log("volume already at the maximum value")
    } else {
      let newVolumeLevel = +this.volume.volume;
      newVolumeLevel = newVolumeLevel + 5;
      if (newVolumeLevel > 100) {
        newVolumeLevel = 100;
      }
      let targetVolume: Volume = { volume: newVolumeLevel.toString() }
      this.settingsService.setVolume(targetVolume).subscribe(
        success => {
          this.refreshVolume();
        },
        error => console.log("Error " + error)
      );
    }
  }
}

