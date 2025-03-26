import matplotlib.pyplot as plt


def show_spending_pie_chart(df, save_path=None):
    expenses = df[df["Type"] == "Debit"]

    category_totals = expenses.groupby("Category")["Amount"].sum().abs()

    if category_totals.empty:
        print("No expense data available to plot.")
        return

    plt.figure(figsize=(8, 6))
    plt.pie(
        category_totals,
        labels=category_totals.index,
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("Spending by Category")
    plt.axis("equal")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()
