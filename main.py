import os
import json
import matplotlib.pyplot as plt
from datetime import datetime

from scripts.daily_spending import add_daily_spending
from scripts.generate_report import generate_monthly_report

DATA_DIR = "data"

def setup():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    current_month = datetime.now().strftime("%Y-%m")
    budget_file = os.path.join(DATA_DIR, f"{current_month}_budget.json")
    
    if not os.path.exists(budget_file):
        budget = float(input("Enter your monthly budget: "))
        with open(budget_file, "w") as file:
            json.dump({"budget": budget, "spending": []}, file)
        print("Budget initialized!")
    else:
        print("Monthly budget already exists!")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add daily spending")
        print("2. Generate month-end report")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_daily_spending()
        elif choice == "2":
            generate_monthly_report()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    setup()
    main_menu()
