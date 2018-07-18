import { TestBed, inject } from '@angular/core/testing';

import { DeviceStateService } from './device-state.service';

describe('DeviceStateService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DeviceStateService]
    });
  });

  it('should be created', inject([DeviceStateService], (service: DeviceStateService) => {
    expect(service).toBeTruthy();
  }));
});
