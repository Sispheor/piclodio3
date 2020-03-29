import '@angular/localize/init'
import { Component, OnInit } from '@angular/core';
import { Webradio } from '../models/webradio';
import { WebRadioService } from '../services/webradio.service';
import { Player } from '../models/player';
import { PlayerService } from '../services/player.service';
import { Router } from '@angular/router';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { ModalConfirmDeletionComponent } from '../modal-confirm-deletion/modal-confirm-deletion.component';

@Component({
  selector: 'app-webradio',
  templateUrl: './webradio.component.html',
  styleUrls: ['./webradio.component.scss']
})
export class WebradioComponent implements OnInit {

  webradios: Webradio[] = [];
  webRadioToDelete: Webradio;
  modalConfirmDeleteWebRadioIsVisible: Boolean = false;
  message: String;
  closeResult = '';

  constructor(private router: Router,
              private webRadioService: WebRadioService,
              private playerService: PlayerService,
              private modalService: NgbModal) { }

  ngOnInit(): void {
    this.refreshWebRadioList();
  }

  setWebRadios(webradios: Webradio[]){
    this.webradios = webradios;
  }

  playWebRadio(webradio: Webradio) {
    console.log("Play web radio id " + webradio.id);
    let player = new Player();
    player.active = true;
    player.webradio = webradio;
    this.playerService.setPlayerStatus(player).subscribe(
      (value) => {
        this.router.navigate(["homepage"]);
      },
      (error) => {
        console.log("Error " + error)
      },
      () => {
        console.log("Observable 'getSystemDate' complete");
      }
    );

  }

  confirmDeleteWebRadio(webradio) {
    this.webRadioToDelete = webradio;
    const modalRef = this.modalService.open(ModalConfirmDeletionComponent);
    modalRef.componentInstance.name = webradio.name;
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
    this.webRadioService.deleteWebradio(this.webRadioToDelete).subscribe(
      (success) => this.refreshWebRadioList(),
      (error) => {
        console.log("Error " + error)
      },
      () => {
        console.log("Observable 'perform_delete' complete");
      }
    )
  }

  refreshWebRadioList(){
    this.webRadioService.getAllWebRadios().subscribe(this.setWebRadios.bind(this));
  }

}
