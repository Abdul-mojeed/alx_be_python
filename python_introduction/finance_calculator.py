# Prompt the user for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Define annual interest rate
interest_rate = 0.05  # 5%

# Project annual savings (including simple interest)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Display results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings after interest are: ${projected_savings:.2f}")
