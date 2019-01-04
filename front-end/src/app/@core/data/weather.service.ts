import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders} from '@angular/common/http'
import { NbAuthService } from '@nebular/auth';
import {environment} from "../../../environments/environment";

export interface Weather{
  windSpeed : number;
  temperature: number;
  humidity: number;
  pressure: number;
  cloudCover:number;
}

@Injectable({
  providedIn: 'root'
})
export class WeatherService {
  private _headers = new HttpHeaders();
  private authToken:string;
  res:Weather;

  url:string = environment.apiEndPoint +'api-get-daily-data'

  constructor(private http:HttpClient,private authService:NbAuthService) { 
    this.authToken=this.authService.getToken()["value"]["token"]
  }

  getWeatherDetails(){
    const headers = this._headers.append('Authorization','Bearer '+this.authToken);
    let promise=new Promise((resolve,reject)=>{
      this.http.get<Weather>(this.url,{headers:headers}).toPromise().then(myResponse=>{
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