import { Routes } from '@angular/router';
import { ExpenseAddEdit } from './expense-add-edit/expense-add-edit';
import { ExpenseGrid } from './expense-grid/expense-grid';
import { ExpenseList } from './expense-list/expense-list';

export const routes: Routes = [
  { path: 'add-expense', component: ExpenseAddEdit},
  { path: 'dashboard', component: ExpenseGrid},
  { path: 'list', component: ExpenseList }

  // 404 route
  // Wild card
];
