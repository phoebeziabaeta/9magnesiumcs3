# Computational Thinking Exercise
### Smart School Canteen Queue
**Name:** Phoebe Zia V. Baeta

**Section:** Magnesium
## Step 1: Identify the Big Problem
### Main Problem:
The current system used is unnecessarily time-consuming and vulnerable to errors that come with manual calculations.
## Step 2: Identify the Sub-Problems
1. Some students take too long to decide what to order, presumably because the menu options are not already displayed.
2. The cashier has to manually calculate totals and give change.
3. There is no system to track which food items are running out.
## Step 3: Define Computational Thinking Approaches
| Sub-Problem | CT Skill/s | Proposed Solution |
| --- | --- | --- |
| Order decision delays | Decomposition | List down all the menu options with their price and display it for students to see and decide their orders in advance. | 
| Manual calculation | Algorithm, Pattern Recognition, and Abstraction | Create a program where the cashier only needs to type the order and simply receives a total price. This can be done by using the algorithm skill to create an organized and simple calculator program, then applying pattern recognition to keep track of products and their prices, and lastly abstraction to hide the calculations and only give the total amount. |
| Stock tracking | Algorithm and Decomposition | List down all the items in stock and develop a program that updates the stock data using mathematical equations. |
## Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
**Sub-Problem chosen:** Manual Calculation
```python
def run_cashier_system():
    menu = {
        "sandwich": 40.00,
        "milo": 25.00,
        "water": 15.00,
        "pizza slice": 60.00,
        "cracklings": 9.00
    }
    
    total_price = 0
    print("Available items:", ", ".join(menu))

    while True:
        item = input("Enter item (or 'done'): ").strip().lower()
        if item == "done":
            break

        if item in menu:
            total_price += menu[item]
        else:
            print("Invalid input")

    print(f"Total: ${total_price:.2f}")

run_cashier_system()

```
