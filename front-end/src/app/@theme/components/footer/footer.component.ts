import { Component } from '@angular/core';

@Component({
  selector: 'ngx-footer',
  styleUrls: ['./footer.component.scss'],
  template: `
    <span class="created-by">Createdby <b><a href="#" target="_blank">Smart Home</a></b> 2017</span>
  `,
})
export class FooterComponent {
}
