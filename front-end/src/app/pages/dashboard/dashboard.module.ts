import { NgModule } from '@angular/core';
import { NgxEchartsModule } from 'ngx-echarts';
import { ThemeModule } from '../../@theme/theme.module';

import { DashboardComponent } from './dashboard.component';
import { StatusCardComponent } from './status-card/status-card.component';
import { RoomsComponent } from './rooms/rooms.component';
import { RoomSelectorComponent } from './rooms/room-selector/room-selector.component';
import { TemperatureDraggerComponent } from './temperature/temperature-dragger/temperature-dragger.component';
import { SecurityCamerasComponent } from './security-cameras/security-cameras.component';
import { ElectricityComponent } from './electricity/electricity.component';
import { WeatherComponent } from './weather/weather.component';
import { PlayerComponent } from './rooms/player/player.component';
import {TemperatureComponent} from './temperature/temperature.component';


@NgModule({
  imports: [
    ThemeModule,
    NgxEchartsModule,
  ],
  declarations: [
    DashboardComponent,
    StatusCardComponent,
    TemperatureDraggerComponent,
    RoomSelectorComponent,
    RoomsComponent,
    SecurityCamerasComponent,
    ElectricityComponent,
    WeatherComponent,
    PlayerComponent,
    TemperatureComponent,
  
  ],
})
export class DashboardModule { }
