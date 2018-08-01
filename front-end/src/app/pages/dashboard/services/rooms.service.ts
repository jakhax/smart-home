import { Injectable } from '@angular/core';
import { resolveDefinition } from '@angular/core/src/view/util';
import {HttpClient} from '@angular/common/http';
import {Device} from '../data/device';
import {DeviceType} from '../data/device-type';
import {Rooms} from '../data/rooms';
import {environment} from "../../../../environments/environment";




@Injectable({
  providedIn: 'root'
})
export class RoomsService {

  url:string=environment.apiEndPoint+"api-get-room"
  allRoomDevicesUrl=environment.apiEndPoint+"api-get-rooms-devices"
  allDeviceTypesUrl=environment.apiEndPoint+"api-get-all-device-types"
  allRoomData=environment.apiEndPoint+"api-get-room-data"

  res:any
  devices:any=[]
  deviceTypes:any=[]
  mycardStyles:any={}
  roomInfo:any={}

  constructor(private http:HttpClient) { 

  }

  getRoomDetails(roomId){
    let promise=new Promise((resolve,reject)=>{
      this.http.get(this.url+'/'+roomId).toPromise().then(myResponse=>{
        this.res=myResponse
        resolve()
      },
    error=>{
      console.log(error)
      reject()
    })
    })
    return promise
  }

  addRoomInfo(a){
    this.roomInfo=[]
    for(var i=0; i<a.length; i++){
      this.roomInfo[a[i]['id']]=new Rooms(a[i]['id'],a[i]['name'])
    }
  }

  addStyeTypes(a){
    this.mycardStyles=[]
    for(var i=0; i<a.length; i++){
      this.mycardStyles[a[i].pk]=new DeviceType(a[i].pk,a[i].fields["name"],a[i].fields["iconclass"],a[i].fields["style_type"])
    }}

  addDeviceTypes(a){
    this.deviceTypes=[]
    for(var i=0; i<a.length; i++){
      this.deviceTypes.push(new DeviceType(a[i].pk,a[i].fields["name"],a[i].fields["iconclass"],a[i].fields["style_type"]))
      }
  }

  addRoomDevices(r){
    this.devices=[]
    for(var i=0;i<r.length;i++){
      this.devices.push(new Device(r[i]["name"],r[i]["id"],r[i]["room"],r[i]["device_type"],r[i]["state"]))
    }
  }  

  getAllDeviceTypes(){
    let promise=new Promise((resolve,reject)=>{
      this.http.get(this.allDeviceTypesUrl).toPromise().then(myResponse=>{
        this.addDeviceTypes(myResponse)
        this.addStyeTypes(myResponse)
        console.log(myResponse)
        resolve()
      },
    error=>{
      console.log(error)
      reject()
    })
    })
    return promise   
  }

getAllRoomDevices(){
  let promise=new Promise((resolve,reject)=>{
    this.http.get(this.allRoomDevicesUrl).toPromise().then(myResponse=>{
      this.addRoomDevices(myResponse)
      resolve()
    },
  error=>{
    console.log(error)
    reject()
  })
  })
  return promise   

}
getAllRoomInfo(){
  let promise=new Promise((resolve,reject)=>{
    this.http.get(this.allRoomData).toPromise().then(myResponse=>{
      this.addRoomInfo(myResponse)
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
