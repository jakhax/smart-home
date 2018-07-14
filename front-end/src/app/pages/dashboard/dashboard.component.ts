import {Component, OnDestroy} from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { takeWhile } from 'rxjs/operators/takeWhile' ;

interface CardSettings {
  title: string;
  iconClass: string;
  type: string;
  status: boolean,
}

@Component({
  selector: 'ngx-dashboard',
  styleUrls: ['./dashboard.component.scss'],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent implements OnDestroy {

  private alive = true;

  aboutMe(me){
    console.log(me)
  }

  lightCard: CardSettings = {
    title: 'Light A',
    iconClass: 'nb-power',
    type: 'warning',
    status: true,
  };
  lightCards: CardSettings = {
    title: 'Light B',
    iconClass: 'nb-lightbulb',
    type: 'primary',
    status: true,
  };
 
  rollerShadesCard: CardSettings = {
    title: 'Roller Shades',
    iconClass: 'nb-roller-shades',
    type: 'success',
    status: true,
  };
  
  wirelessAudioCard: CardSettings = {
    title: 'Wireless Audio',
    iconClass: 'nb-audio',
    type: 'info',
    status: true,
  };


  statusCards: string;

  commonStatusCardsSet: CardSettings[] = [
    this.lightCard,
    this.lightCards,
    this.rollerShadesCard,
    this.wirelessAudioCard,
  
  ];

  statusCardsByThemes: {
    default: CardSettings[];
    cosmic: CardSettings[];
    corporate: CardSettings[];
  } = {
    default: this.commonStatusCardsSet,
    cosmic: this.commonStatusCardsSet,
    corporate: [
      {
        ...this.lightCard,
        type: 'warning',
      },
      {
        ...this.lightCards,
        type: 'warning',
      },
      {
        ...this.rollerShadesCard,
        type: 'primary',
      },
      {
        ...this.wirelessAudioCard,
        type: 'danger',
      },
    ],
  };

  constructor(private themeService: NbThemeService) {
    this.themeService.getJsTheme()
      .pipe(takeWhile(() => this.alive))
      .subscribe(theme => {
        this.statusCards = this.statusCardsByThemes[theme.name];
    });
  }

  ngOnDestroy() {
    this.alive = false;
  }
}
