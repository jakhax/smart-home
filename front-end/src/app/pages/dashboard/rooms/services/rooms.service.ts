import { Injectable } from '@angular/core';
import { resolveDefinition } from '@angular/core/src/view/util';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RoomsService {

  url:string="http://localhost:8000/api-get-room"
  res:any

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
}

