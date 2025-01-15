# Personal Budget Manager

## Overview
This project is a simple web-based personal budget manager. It allows users to:
- Set a monthly budget.
- Add daily spending by category.
- View spending reports with a pie chart visualization.
- Instantly see a detailed list of spending activities.

The project uses **HTML**, **CSS**, and **JavaScript**, and stores data locally using the browser's LocalStorage.

## Features
1. **Monthly Budget Input**: Users can define their monthly budget.
2. **Add Spending**: Users can record spending amounts with specific categories.
3. **Spending List**: Displays all spending details categorized and listed.
4. **Spending Chart**: Pie chart visualization of spending by category.
5. **Data Persistence**: All data is stored locally and reloaded when revisiting the page.

## Technologies Used
- **HTML**: For structuring the webpage.
- **CSS**: For styling the user interface.
- **JavaScript**: For interactivity and logic.
- **Chart.js**: For generating dynamic pie charts.
- **LocalStorage**: For storing user data persistently.

## File Structure
```
personal_budget_manager/
├── index.html       # Main HTML file
├── style.css        # Contains CSS for styling (inline styles included here)
├── script.js        # JavaScript for interactivity and logic
```

## How to Use
1. Clone or download this repository to your local machine.
2. Open the `index.html` file in your preferred web browser.
3. Follow these steps:
   - Enter a monthly budget in the input field.
   - Add spending details by entering a category and an amount.
   - Click "Add Spending" to instantly update the spending list and chart.
4. Review the spending chart and detailed spending list to track your expenses.

## Functionalities
### Adding Spending
- Enter the category and amount spent.
- The chart and spending list are updated dynamically.

### Persistent Data
- The app saves all data locally using LocalStorage.
- Data is automatically loaded when the page is reopened.

## Demo
1. Set your monthly budget, e.g., 5000.
2. Add spending like `Food: 200`, `Transport: 300`.
3. View the pie chart updating with your categories and their proportions.

## Dependencies
- [Chart.js](https://www.chartjs.org/) (Included via CDN).

## Credits
This project was developed as a basic personal budget management tool for educational purposes.

## License
This project is open-source and available under the [MIT License](LICENSE).
