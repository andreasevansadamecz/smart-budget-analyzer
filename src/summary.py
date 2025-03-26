import pandas as pd
from datetime import datetime


def show_monthly_summary(df: pd.DataFrame, month_year: str):
    df["Date"] = pd.to_datetime(df["Date"])

    target_month = datetime.strptime(month_year, "%Y-%m")
    filtered = df[df["Date"].dt.to_period("M") == target_month.strftime("%Y-%m")]

    if filtered.empty:
        print(f"\n No transactions found for {month_year}")
        return

    income = filtered[filtered["Type"] == "Credit"]["Amount"].sum()
    expenses = filtered[filtered["Type"] == "Debit"]["Amount"].sum()
    net = income + expenses

    category_summary = (
        filtered[filtered["Type"] == "Debit"]
        .groupby("Category")["Amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
    )

    print(f"\n===== Summary for {target_month.strftime('%B %Y')} =====")
    print(f"Income:        ${income:.2f}")
    print(f"Expenses:      ${-expenses:.2f}")
    print(f"Net Savings:   ${net:.2f}")
    print("\nTop Categories:")
    for cat, amt in category_summary.items():
        print(f"- {cat:<18} ${amt:.2f}")