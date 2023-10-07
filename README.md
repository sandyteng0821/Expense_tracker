# Expense_tracker
A python command-line tool for life expense tracking

## Description

The Expense Tracker is a Python command-line tool designed to help you record and manage your life expenses. You can use this tool to add, view, reset, and export your expense data. Whether you want to track daily spending or analyze your monthly budget, the Expense Tracker has you covered.

## Table of Contents

- [Installation]
- [Usage]
- [Commands]
- [Arguments]

## Installation

1. Make sure you have Python 3 installed on your system.
2. Clone or download this repository to your local machine.

## Usage

The `ExpenseTracker` program supports the following commands:

### Add an Expense

Use the `add` command to add a new expense. You will be prompted to enter the date, category, and amount of the expense.

```shell
python expense_tracker.py add --db expenses.csv
```

### View Expenses

View your expenses based on optional filters such as month and category using the `view` command.

```shell
python expense_tracker.py view --db expenses.csv --month 5 --category Food
```

### Reset Expenses

Reset your expense file to start fresh with the `reset` command.

```shell
python expense_tracker.py reset --db expenses.csv
```

### Export to Excel

Export your expenses to an Excel file (default: expenses.xlsx) using the `export` command. Specify the output file name with the `--output_file` option.

```shell
python expense_tracker.py export --db expenses.csv --output_file expenses.xlsx
```

## Arguments

- `--db`: Specify the input expense record file (a CSV file with existing expenses). This argument is required for all commands.
- `--month`: View expenses for a specific month (1-12).
- `--category`: View expenses for a specific category.
- `--output_file`: Specify the output file for exporting expenses.

### Demo
```
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py reset --db D:\Python-programming\expenses.csv
Expense file reset.
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py add --db D:\Python-programming\expenses.csv
Enter expense category: Food
Enter expense amount ($): 150
Expense added successfully.
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py add --db D:\Python-programming\expenses.csv
Enter expense category: Food
Enter expense amount ($): 70
Expense added successfully.
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py add --db D:\Python-programming\expenses.csv
Enter expense category: Housing
Enter expense amount ($): 10000
Expense added successfully.
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py add --db D:\Python-programming\expenses.csv
Enter expense category: Groceries
Enter expense amount ($): 80
Expense added successfully.
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py add --db D:\Python-programming\expenses.csv
Enter expense category: Groceries
Enter expense amount ($): 90
Expense added successfully.
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py view --db D:\Python-programming\expenses.csv
Expenses:
Date: 2023-10-07, Category: Food, Amount: $150
Date: 2023-10-07, Category: Food, Amount: $70
Date: 2023-10-07, Category: Housing, Amount: $10000
Date: 2023-10-07, Category: Groceries, Amount: $80
Date: 2023-10-07, Category: Groceries, Amount: $90
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py export --db D:\Python-programming\expenses.csv
Please specify the output Excel directory using the --output_file option.
PS C:\Users\USER> python D:\Python-programming\expense_tracker.py export --db D:\Python-programming\expenses.csv --output_file D:\Python-programming\expense_tracker.xlsx   Expenses exported to D:\Python-programming\expense_tracker.xlsx.
```

## Author

- Author: sandyteng
- Email: sandy9898@gmail.com

Enjoy tracking your expenses with the Expense Tracker!
