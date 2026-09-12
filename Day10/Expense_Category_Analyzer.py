#Expense Category Analyzer
# Total expense for each category
# The category with the highest total
# The category with the lowest total
# Overall total expense
# Average expense per category


expenses = {
    "food": [250, 120, 300],
    "travel": [500, 200],
    "shopping": [1000, 750],
    "bills": [800, 450]
}

for category, amt in expenses.items():
    total = sum(amt)
    print(f"Total expense for {category}: {total}")

    highest = max(amt)
    print(f"Highest expense in {category}: {highest}")

    lowest = min(amt)
    print(f"Lowest expense in {category}: {lowest}")

    overall_total = sum(sum(amt) for amt in expenses.values())
    print(f"Overall total expense: {overall_total}")

    average = overall_total / len(expenses)
    print(f"Average expense per category: {average}")
