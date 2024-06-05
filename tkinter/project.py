import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Expense:
    def __init__(self, date, amount, description, category):
        self.date = date
        self.amount = amount
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.date} - {self.description}: RS:{self.amount:.2f} [{self.category.name}]"

class Category:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def __str__(self):
        return f"Category: {self.name}, Total Expenses: RS{self.total_expenses():.2f}"

class ExpenseManager:
    def __init__(self):
        self.categories = {}

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = Category(category_name)

    def add_expense(self, date, amount, description, category_name):
        if category_name not in self.categories:
            self.add_category(category_name)
        category = self.categories[category_name]
        expense = Expense(date, amount, description, category)
        category.add_expense(expense)

    def get_total_expenses(self):
        return sum(category.total_expenses() for category in self.categories.values())

    def generate_report(self):
        report = "Expense Report:\n"
        for category in self.categories.values():
            report += str(category) + "\n"
            for expense in category.expenses:
                report += "  " + str(expense) + "\n"
        report += f"Total Expenses: RS:{self.get_total_expenses():.2f}\n"
        return report

class ExpenseApp:
    def __init__(self, root):
        self.manager = ExpenseManager()
        self.root = root
        self.root.title("Expense Tracker")

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=2, column=1, padx=10, pady=5)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.report_button = tk.Button(root, text="Generate Report", command=self.show_report)
        self.report_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.report_text = tk.Text(root, width=50, height=20)
        self.report_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def add_expense(self):
        try:
            date = datetime.strptime(self.date_entry.get(), "%Y-%m-%d")
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()
            category = self.category_entry.get()

            self.manager.add_expense(date, amount, description, category)
            messagebox.showinfo("Success", "Expense added successfully!")

            self.date_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def show_report(self):
        report = self.manager.generate_report()
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, report)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()
