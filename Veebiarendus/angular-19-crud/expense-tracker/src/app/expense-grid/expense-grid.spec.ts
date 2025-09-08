import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExpenseGrid } from './expense-grid';

describe('ExpenseGrid', () => {
  let component: ExpenseGrid;
  let fixture: ComponentFixture<ExpenseGrid>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ExpenseGrid]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExpenseGrid);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
