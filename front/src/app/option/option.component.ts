import { PopupComponent } from './../popup/popup.component';
import { Backup } from './backup';
import { GlobalVariable } from './../globals';
import { Volume } from './volume';
import { OptionService } from './option.service';
import { Component, OnInit, ViewChild } from '@angular/core';
import { FileUploader } from 'ng2-file-upload';

@Component({
  selector: 'app-option',
  templateUrl: './option.component.html',
  styleUrls: ['./option.component.css']
})
export class OptionComponent implements OnInit {
  baseUrl: string = GlobalVariable.BASE_API_URL;
  currentVolume: Volume;
  currentBackup: Backup;
  volumeLoaded: boolean = false;
  public uploader: FileUploader = new FileUploader({
    url: this.baseUrl + "/backup",
    method: 'POST',
    itemAlias: 'backup_file',
    queueLimit: 1,
    removeAfterUpload: true
  });
  @ViewChild(PopupComponent) popupComponent: PopupComponent;

  constructor(private optionService: OptionService) {

    // action when we successfully upload a file
    this.uploader.onSuccessItem = () => {
      console.log('upload complete');
      // refresh the view
      this.refreshBackup();
      // show a popup message
      this.popupComponent.add('success', 'File uploaded');
    };

    // action when we failled to upload a file
    this.uploader.onErrorItem = () => {
      console.log('upload failled');
      // show a popup message
      this.popupComponent.add('danger', 'Fail to upload');
    };

  }

  ngOnInit() {
    // get the current volume
    this.refreshVolume();
    // get the current backup file
    this.refreshBackup();
    // set CORS to *
    this.uploader.onBeforeUploadItem = (item) => {
      item.withCredentials = false;
    }

  }

  /**
   * Load the view with the received backup file
   */
  refreshBackup() {
    this.optionService.getBackup().subscribe(this.setBackup.bind(this));
  }

  /**
   * Load the view with the received volume
   */
  refreshVolume() {
    this.optionService.getVolume().subscribe(this.setVolume.bind(this));
  }

  /**
   * Bind the reveiced data to the view
   */
  setVolume(volume: Volume) {
    this.currentVolume = volume;
    this.volumeLoaded = true;
  }

  /**
   * Bind the reveiced data to the view
   * The data contains a full path, the method will only keep the file name
   */
  setBackup(backup: Backup[]) {
    console.log("Recevied backup: ");
    console.log(backup);
    if (typeof backup !== 'undefined' && backup.length > 0) {
      // the array is defined and has at least one element
      console.log(backup[0]);
      // we receive a complete path that contain the root path and the file name. let's keep only the file name
      let tmpBackup = backup[0];
      let onlyFileName = tmpBackup.backup_file.split('/')[1];
      tmpBackup.backup_file = onlyFileName;
      this.currentBackup = tmpBackup;
    }

  }

  /**
   * Call the backend to reduce the volume
   */
  reduceVolume() {
    let newVolumeLevel = this.currentVolume.volume;
    newVolumeLevel = newVolumeLevel - 10;
    if (newVolumeLevel < 0) {
      newVolumeLevel = 0;
    }
    this.currentVolume.volume = newVolumeLevel
    this.optionService.setVolume(this.currentVolume).subscribe(
      success => {
        this.refreshVolume();
      },
      error => console.log("Error " + error)
    );
  }

  /**
   * Call the backend to increase the volume
   */
  increaseVolume() {
    let newVolumeLevel = this.currentVolume.volume;
    newVolumeLevel = newVolumeLevel + 10;
    if (newVolumeLevel > 100) {
      newVolumeLevel = 100;
    }
    this.currentVolume.volume = newVolumeLevel
    this.optionService.setVolume(this.currentVolume).subscribe(
      success => {
        this.refreshVolume();
      },
      error => console.log("Error " + error)
    );
  }

}
