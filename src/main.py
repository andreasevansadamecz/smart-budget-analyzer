import os
from parser import load_transactions
from categorizer import categorize_transactions
from visualizer import show_spending_pie_chart
from summary import show_monthly_summary

DATA_PATH = os.path.join("..", "data", "sample_bank.csv")


def main():
    transactions = load_transactions(DATA_PATH)

    if transactions is None:
        print("No data available to analyze.")
        return

    transactions = categorize_transactions(transactions)

    print("\n=== Transaction Overview ===")
    print(transactions[["Date", "Description", "Amount", "Type", "Category"]])

    income = transactions[transactions["Type"] == "Credit"]["Amount"].sum()
    expenses = transactions[transactions["Type"] == "Debit"]["Amount"].sum()

    print(f"\nTotal Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")

    print("\n=== Spending by Category ===")
    category_summary = transactions[transactions["Type"] == "Debit"].groupby("Category")["Amount"].sum()
    print(category_summary)

    show_spending_pie_chart(transactions)

    month_input = input("\n View monthly summary? Enter YYYY-MM (e.g. 2025-03), or press Enter to skip: ")
    if month_input:
        show_monthly_summary(transactions, month_input)


if __name__ == "__main__":
    main()
