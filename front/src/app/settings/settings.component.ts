import { Component, OnInit } from '@angular/core';
import { SettingsService } from '../services/settings.service';
import { Volume } from '../models/volume';
import { Backup } from '../models/backup';
import { ToastService } from '../services/toast.service';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.scss']
})
export class SettingsComponent implements OnInit {

  volumeLoaded = false;
  volume: Volume = { volume: "0"};
  backupFileName: string = ""
  fileToUpload: File = null;

  constructor(private settingsService: SettingsService,
              public toastService: ToastService) { }

  ngOnInit(): void {
    this.refreshVolume();
    this.refreshBackup();
  }

  refreshVolume() {
    this.settingsService.getVolume().subscribe(this.setVolume.bind(this));
  }
  refreshBackup() {
    this.settingsService.getBackup().subscribe(this.setBackup.bind(this));
  }

  setVolume(volume: Volume) {
    this.volume = volume;
    this.volumeLoaded = true;
  }

  setBackup(backupList: Backup[]){
    if (typeof backupList !== 'undefined' && backupList.length > 0) {
      // the array is defined and has at least one element
      console.log(backupList[0]);
      // we receive a complete path that contain the root path and the file name. let's keep only the file name
      let tmpBackup = backupList[0];
      this.backupFileName = tmpBackup.backup_file.split('/')[1];
    }
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

  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }

  uploadFileToActivity() {
    this.settingsService.postFile(this.fileToUpload).subscribe(data => {
      this.toastService.show('File uploaded successfully', { classname: 'bg-info text-light', delay: 5000 });
      this.refreshBackup();
    }, error => {
      console.log(error);
      this.toastService.show('Error while uploading', { classname: 'bg-danger text-light', delay: 5000 });
    });
  }
}

