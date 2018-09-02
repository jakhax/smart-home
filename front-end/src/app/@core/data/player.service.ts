import { Injectable } from '@angular/core';
import {environment} from '../../../environments/environment';
import {HttpClient,HttpHeaders} from '@angular/common/http'
import { NbAuthService } from '@nebular/auth';

export class Track {
  name: string;
  artist: string;
  url: string;
  cover: string;
}

@Injectable()
export class PlayerService {

  private _headers = new HttpHeaders();
  private authToken:string;

  current: number;
  songUrl: string=environment.apiEndPoint+"api-get-music"
  songs:any
  constructor(private http:HttpClient,private authService:NbAuthService) { 
    this.authToken=this.authService.getToken()["value"]["token"]
  }

  playlist: Track[] = [
 
  ];
  

  addSongsTrack(r){
    for(var i=0; i<r.length; i++){
      this.playlist.push(    {
        name: r[i]['name'],
        artist: 'Alabama Shakes',
        url: environment.apiEndPoint+r[i]['url'],
        cover: 'assets/images/cover1.jpg',
      })
      
  }
  }

  getSongs(){
    const headers = this._headers.append('Authorization','Bearer '+this.authToken);
    let promise=new Promise((resolve,reject)=>{
 
      this.http.get(this.songUrl,{headers:headers}).toPromise().then(myResponse=>{
        this.songs=myResponse
        this.addSongsTrack(this.songs)
        resolve()
      },
      error=>{
        console.log(error)
        reject()
    })
    })
    return promise   
  }



  random(): Track {
    this.current = Math.floor(Math.random() * this.playlist.length);
    return this.playlist[this.current];
  }

  next(): Track {
    return this.getNextTrack();
  }

  prev() {
    return this.getPrevTrack();
  }

  private getNextTrack(): Track {
    if (this.current === this.playlist.length - 1) {
      this.current = 0;
    } else {
      this.current++;
    }

    return this.playlist[this.current];
  }

  private getPrevTrack(): Track {
    if (this.current === 0) {
      this.current = this.playlist.length - 1;
    } else {
      this.current--;
    }

    return this.playlist[this.current];
  }
}

