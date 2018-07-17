import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DeviceStateService {
  deviceUrl:string="http://localhost:8000/api-change-device-state/"
  newState:boolean;
  constructor(private http:HttpClient) { }

  changeDeviceState(deviceId){
    let promise=new Promise((resolve,reject)=>{
      this.http.get(this.deviceUrl+deviceId).toPromise().then(myResponse=>{
        this.newState=myResponse["state"]
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
