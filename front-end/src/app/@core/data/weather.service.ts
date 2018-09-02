import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders} from '@angular/common/http'
import { NbAuthService } from '@nebular/auth';
import {environment} from "../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class WeatherService {
  private _headers = new HttpHeaders();
  private authToken:string;
  res;

  url:string = environment.apiEndPoint +'api-get-daily-data'

  constructor(private http:HttpClient,private authService:NbAuthService) { 
    this.authToken=this.authService.getToken()["value"]["token"]
  }

  getWeatherDetails(){
    const headers = this._headers.append('Authorization','Bearer '+this.authToken);
    let promise=new Promise((resolve,reject)=>{
      this.http.get(this.url,{headers:headers}).toPromise().then(myResponse=>{
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