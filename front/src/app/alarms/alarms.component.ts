import { Component, OnInit } from '@angular/core';
import { Alarm } from '../models/alarm';
import { AlarmsService } from '../services/alarms.service';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { ModalConfirmDeletionComponent } from '../modal-confirm-deletion/modal-confirm-deletion.component';

@Component({
  selector: 'app-alarms',
  templateUrl: './alarms.component.html',
  styleUrls: ['./alarms.component.scss']
})
export class AlarmsComponent implements OnInit {

  alarms: Alarm[] = [];
  alarmToDelete: Alarm;
  closeResult = '';

  constructor(private alarmsService: AlarmsService,
              private modalService: NgbModal) { }

  ngOnInit(): void {
    this.refreshAlarmClockList();
  }

  refreshAlarmClockList() {
    this.alarmsService.getAlarms().subscribe(this.setAlarmClocks.bind(this));
  }

  setAlarmClocks(alarms: Alarm[]) {
    console.log(alarms)
    this.alarms = alarms;
  }

  switchAlarmStatus(alarm: Alarm){
    if (alarm.enabled) {
      alarm.enabled = false
    } else {
      alarm.enabled = true
    }
    // update the alarm
    this.alarmsService.updateAlarm(alarm).subscribe(
      success => {
        this.refreshAlarmClockList();
      },
      error => console.log("Error " + error)
    );
  }

  confirmDeleteAlarm(alarm) {
    this.alarmToDelete = alarm;
    const modalRef = this.modalService.open(ModalConfirmDeletionComponent);
    modalRef.componentInstance.name = alarm.name;
    modalRef.result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
      if (result == "confirm click") {
        this.perform_delete()
      }
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return `with: ${reason}`;
    }
  }

  perform_delete(){
    this.alarmsService.deleteAlarm(this.alarmToDelete).subscribe(
      (success) => this.refreshAlarmClockList(),
      (error) => {
        console.log("Error " + error)
      },
      () => {
        console.log("Observable 'perform_delete' complete");
      }
    )
  }



}
