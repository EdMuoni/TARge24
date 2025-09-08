import { Injectable, signal } from '@angular/core';
import { Expense } from '../models/expense.model';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ExpenseService {

  private expenseSignal = signal<Expense[]>([]);

  constructor(private http: HttpClient) {}

  // get all expenses
  getExpenses() {
    this.http.get<Expense[]>('http://localhost:3000/expenses')
    .subscribe(expenses => {this.expenseSignal.set(expenses)});
  }

  get expenses() {
    return this.expenseSignal;
  }

  // add expense
  addExpense(expense: Expense) {
  this.http.post<Expense>('http://localhost:3000/expenses', expense)
  .subscribe(()=> this.getExpenses());
  }

  //Delete an Expense
  deleteExpense(id: number) {
    this.http.delete(`http://localhost:3000/expenses/${id}`)
    .subscribe(() => this.getExpenses());
  }

  //Update an Expense
  updateExpense(id: string, updateExpense: Expense) {
    this.http.put<Expense>(`http://localhost:3000/expenses/${id}`, updateExpense)
    .subscribe(() => this.getExpenses());
  }

  //Get Expense by Id
  getExpenseById(id: number) {
    return this.expenseSignal().find(expense => expense.id === id);
  }
}
