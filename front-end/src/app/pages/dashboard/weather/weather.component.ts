import { Component,OnInit } from '@angular/core';
import { WeatherService,Weather } from '../../../@core/data/weather.service'
@Component({
  selector: 'ngx-weather',
  styleUrls: ['./weather.component.scss'],
  templateUrl: './weather.component.html',
})


export class WeatherComponent {
  data:Weather
  todayDate= new Date()
  constructor(private myservice:WeatherService){
     
  }
  // getData(){
   
  // }
  ngOnInit(): void {
    //Called after the constructor, initializing input properties, and the first call to ngOnChanges.
    //Add 'implements OnInit' to the class.
    this.myservice.getWeatherDetails().then(()=>{
      this.data = this.myservice.res
      // console.log(this.data)
    })
  }
}