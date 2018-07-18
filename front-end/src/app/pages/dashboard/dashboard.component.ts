import {Component, OnDestroy,OnInit} from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { takeWhile } from 'rxjs/operators/takeWhile' ;
import {RoomsService} from './services/rooms.service';
import {DeviceStateService} from "./services/device-state.service";


interface CardSettings {
  id:number;
  title: string;
  iconClass: string;
  type: string;
  status: boolean;
}

@Component({
  selector: 'ngx-dashboard',
  styleUrls: ['./dashboard.component.scss'],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent implements OnDestroy {

  private alive = true;

  selectControl(control){
    var devices=this.getAllDevices.devices
    this.deviceState.changeDeviceState(control.id).then(()=>{
      control.status=this.deviceState.newState
      for (var i=0;i<devices.length;i++){
        if(devices[i].id===control.id){
          devices[i].state=control.status
        }
      }
      console.log(control)
    })

  }

  selectRoomD(num){
    this.addCardDevices(num)
  }


  statusCards: string;
  sCard:any;
  commonStatusCardsSet: CardSettings[] = [];

  addCardDevices(num){
    this.sCard=[]
    var devices=this.getAllDevices.devices
    var mycards=this.getAllDevices.mycardStyles
    var roomName = this.getAllDevices.roomInfo[num]['name']
    for(var i=0;i<devices.length;i++){
      if(roomName===devices[i].roomName){
        var c={id:devices[i].id,
                title:devices[i].title,
                iconClass:mycards[devices[i].deviceType].icon,
                type:mycards[devices[i].deviceType].style,
                status:devices[i].state
                }
        
        this.sCard.push(c)
      }
      this.statusCards = this.sCard
    }
  }

  statusCardsByThemes: {
    default: CardSettings[];
    cosmic: CardSettings[];
    
  } = {
    default: this.commonStatusCardsSet,
    cosmic: this.commonStatusCardsSet,
  };

  constructor(private themeService: NbThemeService,
    private getAllDevices:RoomsService,
    private deviceState:DeviceStateService) {

  }

  ngOnDestroy() {
    this.alive = false;
  }
  ngOnInit(){
    this.getAllDevices.getAllDeviceTypes().then(()=>{
      // console.log(this.getAllDevices.deviceTypes);
      // console.log(this.getAllDevices.mycardStyles);
      this.getAllDevices.getAllRoomInfo().then(()=>{
        console.log(this.getAllDevices.roomInfo)
        this.getAllDevices.getAllRoomDevices().then(()=>{
          // console.log(this.getAllDevices.devices);
          this.addCardDevices(2)
          console.log(this.commonStatusCardsSet)
        })
      })
    })
  }

}