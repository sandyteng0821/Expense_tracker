#!/usr/bin/python3
#======
#
# Program: Life expense tracker
# Usage: python expense_tracker.py
#        python expense_tracker.py -h
#        python expense_tracker.py view --db D:\Python-programming\expenses.csv
#        python expense_tracker.py add --db D:\Python-programming\expenses.csv (enter date, catergory and amount)
#       
# Description: a python command line tool to add and view life expense
# Author: sandyteng 
#
#======
class ExpenseTracker:
    def __init__(self, args={}):
        self.args = {}
        self.args.update(args)
        self.prepare()

    def prepare(self):
        self.month = self.args.get('month')
        self.category = self.args.get('category')
        self.expenserecord = self.args.get('db')

    def add_expense(self, date, category, amount):
        with open(self.expenserecord, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])

    def view_expenses(self):
        try:
            with open(self.expenserecord, mode='r') as file:
                reader = csv.reader(file)
                #header = next(reader)  # Skip the header row
                expenses = [row for row in reader]

            if not expenses:
                print("No expenses recorded yet.")
                return

            filtered_expenses = []

            for expense in expenses:
                expense_date = datetime.datetime.strptime(expense[0], '%Y-%m-%d')
                if (not self.month or expense_date.month == self.month) and (
                        not self.category or expense[1] == self.category):
                    filtered_expenses.append(expense)

            if not filtered_expenses:
                print("No matching expenses found.")
            else:
                print("Expenses:")
                for row in filtered_expenses:
                    print(f"Date: {row[0]}, Category: {row[1]}, Amount: ${row[2]}")
        except FileNotFoundError:
            print("No expenses recorded yet.")

    def reset_expenses(self):
        try:
            os.remove(self.expenserecord)
            print("Expense file reset.")
        except FileNotFoundError:
            print("Expense file not found.")

    def export_to_excel(self, output_file=None):
        if not output_file:
            print("Please specify the output Excel directory using the --output_file option.")
            return
        try:
            with open(self.expenserecord, mode='r') as file:
                df = pd.read_csv(file, header=None)
                df.columns = ["Date", "Category", "Amount"]
                output_file = os.path.join(os.getcwd(),output_file)  # Set output file in the current directory
                df.to_excel(output_file, index=False)
            print(f"Expenses exported to {output_file}.")
        except FileNotFoundError:
            print("No expenses recorded yet.")

    def main(self):
        if self.args['command'] == 'add':
            date = datetime.date.today().strftime('%Y-%m-%d')
            category = input('Enter expense category: ')
            amount = input('Enter expense amount ($): ')
            self.add_expense(date, category, amount)
            print('Expense added successfully.')

        elif self.args['command'] == 'view':
            self.view_expenses()

        elif self.args['command'] == 'reset':
            self.reset_expenses()

        elif self.args['command'] == 'export':
            self.export_to_excel(self.args.get('output_file'))

if __name__ == '__main__':
    import os
    import csv
    import argparse
    import datetime
    import pandas as pd    
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description='Record and manage life expenses.')
    parser.add_argument('command', choices=['add', 'view', 'reset', 'export'],
                        help='Command: "add" to add an expense, "view" to view expenses, '
                             '"reset" to reset the expense file, "export" to export expenses to Excel')
    parser.add_argument('--db', type=str, help= 'Please specify the input expense record file (csv file with rows of existing expenses)', required=True)
    parser.add_argument('--month', type=int, help='View expenses for a specific month (1-12)')
    parser.add_argument('--category', help='View expenses for a specific category')
    parser.add_argument('--output_file', help='Specify the output file for exporting expenses')
    args = parser.parse_args()

    # Create an instance of ExpenseTracker and call the main method
    expense_tracker = ExpenseTracker(vars(args))
    expense_tracker.main()