import { Injectable } from '@angular/core';
import { resolveDefinition } from '@angular/core/src/view/util';
import {HttpClient} from '@angular/common/http';
import {Device} from '../data/device';
import {DeviceType} from '../data/device-type';
import {Rooms} from '../data/rooms';




@Injectable({
  providedIn: 'root'
})
export class RoomsService {

  url:string="http://localhost:8000/api-get-room"
  allRoomDevicesUrl="http://localhost:8000/api-get-all-rooms"
  allDeviceTypesUrl="http://localhost:8000/api-get-all-device-types"
  allRoomData="http://localhost:8000/api-get-room-data"

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
    for(var i=0; i<a.length; i++){
      this.roomInfo[a[i]['id']]=new Rooms(a[i]['id'],a[i]['name'])
    }
  }

  addStyeTypes(a){
    for(var i=0; i<a.length; i++){
      this.mycardStyles[a[i].pk]=new DeviceType(a[i].pk,a[i].fields["name"],a[i].fields["iconclass"],a[i].fields["style_type"])
    }}

  addDeviceTypes(a){
    for(var i=0; i<a.length; i++){
      this.deviceTypes.push(new DeviceType(a[i].pk,a[i].fields["name"],a[i].fields["iconclass"],a[i].fields["style_type"]))
      }
  }

  addRoomDevices(r){
    for(var i=0;i<r.length;i++){
      this.devices.push(new Device(r[i].fields["name"],r[i].pk,r[i].fields["room"],r[i].fields["device_type"],r[i].fields["state"]))
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
