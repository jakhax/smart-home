import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders} from '@angular/common/http'
import { NbAuthService } from '@nebular/auth';
import {environment} from "../../../../environments/environment";

export interface Room {
  id: string;
  name: string;
}

export interface DeviceType {
  name: string;
  iconclass: string;
  style_type: string;
}

export interface Device {
  id: number;
  device_type: DeviceType;
  room: string;
  name: string;
  state: boolean;
}

export interface SmartHome {
  rooms: Room[];
  devices: Device[];
}


@Injectable({
  providedIn: 'root'
})
export class SmartHomeService {
  private _headers = new HttpHeaders();
  private authToken:string;

  smartHomeInfo:SmartHome
  smartHomeInfoUrl= environment.apiEndPoint + "api-get-smart-home-info"

  constructor(private http:HttpClient,private authService:NbAuthService) { 
    this.authToken=this.authService.getToken()["value"]["token"]
  }

  getSmartHomeInfo(){
    const headers = this._headers.append('Authorization','Bearer '+this.authToken);
    let promise=new Promise((resolve,reject)=>{
      this.http.get<SmartHome>(this.smartHomeInfoUrl,{headers:headers}).toPromise().then(myResponse=>{
        this.smartHomeInfo=myResponse
        resolve()
      },
    error=>{
      console.log(error)
      reject()
    })
    })
    return promise   
    }
  
}


