import { NgModule, ModuleWithProviders } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ElectricityService } from './electricity.service';
import { StateService } from './state.service';
import { PlayerService } from './player.service';
import { LayoutService } from './layout.service';
import { WeatherService } from './weather.service';

const SERVICES = [
  ElectricityService,
  StateService,
  PlayerService,
  LayoutService,
  WeatherService,
];

@NgModule({
  imports: [
    CommonModule,
  ],
  providers: [
    ...SERVICES,
  ],
})
export class DataModule {
  static forRoot(): ModuleWithProviders {
    return <ModuleWithProviders>{
      ngModule: DataModule,
      providers: [
        ...SERVICES,
      ],
    };
  }
}