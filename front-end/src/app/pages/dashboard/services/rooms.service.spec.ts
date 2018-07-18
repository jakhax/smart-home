import { TestBed, inject } from '@angular/core/testing';

import { RoomsService } from './rooms.service';

describe('RoomsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RoomsService]
    });
  });

  it('should be created', inject([RoomsService], (service: RoomsService) => {
    expect(service).toBeTruthy();
  }));
});
