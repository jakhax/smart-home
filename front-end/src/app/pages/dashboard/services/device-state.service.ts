import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders} from '@angular/common/http'
import { NbAuthService } from '@nebular/auth';
import {environment} from "../../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class DeviceStateService {
  private _headers = new HttpHeaders();
  private authToken:string;
  deviceUrl:string=environment.apiEndPoint+"api-change-device-state/"
  newState:boolean;
  constructor(private http:HttpClient,private authService:NbAuthService) { 
    this.authToken=this.authService.getToken()["value"]["token"]
  }

  changeDeviceState(deviceId){
    const headers = this._headers.append('Authorization','Bearer '+this.authToken);
    let promise=new Promise((resolve,reject)=>{
      this.http.get(this.deviceUrl+deviceId,{headers:headers}).toPromise().then(myResponse=>{
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
