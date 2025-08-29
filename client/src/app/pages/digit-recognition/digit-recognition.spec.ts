import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DigitRecognition } from './digit-recognition';

describe('DigitRecognition', () => {
  let component: DigitRecognition;
  let fixture: ComponentFixture<DigitRecognition>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DigitRecognition]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DigitRecognition);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
