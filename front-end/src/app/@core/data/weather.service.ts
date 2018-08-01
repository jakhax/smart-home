import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from "../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class WeatherService {
  res;

  url:string = environment.apiEndPoint +'api-get-daily-data'

  constructor(private http:HttpClient) { }
  getWeatherDetails(){
    let promise=new Promise((resolve,reject)=>{
      this.http.get(this.url).toPromise().then(myResponse=>{
        this.res=myResponse
        console.log(this.res)
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