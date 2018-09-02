import { TestBed, inject } from '@angular/core/testing';

import { SmartHomeService } from './smart-home.service';

describe('RoomsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SmartHomeService]
    });
  });

  it('should be created', inject([SmartHomeService], (service: SmartHomeService) => {
    expect(service).toBeTruthy();
  }));
});
