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

## Author

- Author: sandyteng
- Email: sandy9898@gmail.com

Enjoy tracking your expenses with the Expense Tracker!
