import {Component, OnDestroy,OnInit} from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { takeWhile } from 'rxjs/operators/takeWhile' ;
import {SmartHomeService} from './services/smart-home.service';
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
    var devices=this.smartHomeService.smartHomeInfo.devices
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
    var devices=this.smartHomeService.smartHomeInfo.devices
    var roomName = this.smartHomeService.smartHomeInfo.rooms[num].name
    for(var i=0;i<devices.length;i++){
      if(roomName===devices[i].room){
        var c={id:devices[i].id,
                title:devices[i].name,
                iconClass:devices[i].device_type.iconclass,
                type:devices[i].device_type.style_type,
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
    private smartHomeService:SmartHomeService,
    private deviceState:DeviceStateService) {

  }
  loadSmartHomeInfo(){
    this.smartHomeService.getSmartHomeInfo().then(()=>{
      if(this.smartHomeService.smartHomeInfo.devices.length>0){
        this.addCardDevices(this.smartHomeService.smartHomeInfo.devices[0].id)
      }
    }).catch(error =>{
      console.log(error)
    })
  }
  ngOnDestroy() {
    this.alive = false;
  }
  ngOnInit(){
    this.loadSmartHomeInfo()
  }
}