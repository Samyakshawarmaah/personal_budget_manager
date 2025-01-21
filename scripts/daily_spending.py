import os
import json
from datetime import datetime

DATA_DIR = "data"

def add_daily_spending():
    current_month = datetime.now().strftime("%Y-%m")
    budget_file = os.path.join(DATA_DIR, f"{current_month}_budget.json")
    
    if not os.path.exists(budget_file):
        print("No budget found for this month. Please initialize the budget first!")
        return
    
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the spending category (e.g., Food, Rent, etc.): ")
    amount = float(input("Enter the amount spent: "))
    
    with open(budget_file, "r") as file:
        data = json.load(file)
    
    data["spending"].append({"date": date, "category": category, "amount": amount})
    
    with open(budget_file, "w") as file:
        json.dump(data, file)
    
    print("Spending added successfully!")
