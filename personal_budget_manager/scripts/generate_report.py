import os
import json
import matplotlib.pyplot as plt

def generate_monthly_report():
    # Define paths
    data_dir = "data"
    reports_dir = "reports"
    month = "2025-01"
    budget_file = os.path.join(data_dir, f"{month}_budget.json")
    report_file = os.path.join(reports_dir, f"{month}_report.png")

    # Ensure the reports directory exists
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # Load budget and spending data
    if not os.path.exists(budget_file):
        print("No budget data found for the month.")
        return

    with open(budget_file, "r") as f:
        data = json.load(f)

    # Extract data for analysis
    budget = data.get("budget", 0)
    spending = data.get("spending", {})
    total_spent = sum(spending.values())
    savings = budget - total_spent
    categories = list(spending.keys())
    amounts = list(spending.values())

    # Plot data
    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title(f"Spending Breakdown for {month}\nTotal Spent: ${total_spent:.2f}, Savings: ${savings:.2f}")
    plt.tight_layout()

    # Save the report
    plt.savefig(report_file)
    plt.close()

    print(f"Monthly report saved to {report_file}")
