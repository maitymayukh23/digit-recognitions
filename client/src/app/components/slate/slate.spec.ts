import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Slate } from './slate';

describe('Slate', () => {
  let component: Slate;
  let fixture: ComponentFixture<Slate>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Slate]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Slate);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
