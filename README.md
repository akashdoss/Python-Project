# Smart Expense Tracker (Python)

This is a simple command-line based expense tracker built using Python. The goal of this project is to understand how daily expenses can be recorded, stored, and analyzed in a structured way.

## Overview

Managing personal expenses can get confusing if not tracked properly. This project helps in logging daily spending, categorizing expenses, and generating useful insights like monthly totals and category-wise distribution.

## Features

* Add daily expenses with date, category, amount, and description
* Store data in a CSV file
* View category-wise expense summary
* Calculate total expenses for a specific month
* Identify the highest spending category
* Visualize spending using a pie chart

## Technologies Used

* Python
* CSV (for data storage)
* Matplotlib (for visualization)

## How It Works

The application runs in a loop where the user can choose different options from the menu. Based on the input, the program either adds a new expense or analyzes the existing data stored in the CSV file.

## How to Run

1. Make sure Python is installed

2. Install matplotlib if not already installed:
   pip install matplotlib

3. Run the program:
   python main.py

## Sample Menu

1. Add Expense
2. View Category Summary
3. Monthly Summary
4. Show Pie Chart
5. Exit

## File Structure

* main.py → main program file
* expenses.csv → stores all expense data

## Learning Outcome

This project helped me understand:

* File handling using CSV in Python
* Working with dictionaries for data aggregation
* Basic data visualization
* Building a simple CLI-based application

## Future Improvements

* Add budget limit alerts
* Improve input validation
* Convert to GUI using Tkinter
* Add smart suggestions based on spending patterns

## Conclusion

This is a beginner-friendly project that gives a clear idea of how real-world applications can be built using simple Python concepts.
