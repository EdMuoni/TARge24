import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExpenseAddEdit } from './expense-add-edit';

describe('ExpenseAddEdit', () => {
  let component: ExpenseAddEdit;
  let fixture: ComponentFixture<ExpenseAddEdit>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ExpenseAddEdit]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExpenseAddEdit);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
