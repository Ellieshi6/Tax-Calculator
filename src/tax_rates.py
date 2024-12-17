
TAX_BRACKETS = [
  (0, 18200, 0),
  (18201, 45000, 0.16),
  (45001, 135000, 0.30),
  (135001, 190000, 0.37),
  (190001, float('inf'), 0.45),
]

# calculates user's taxable income using user_data
def calculate_tax(taxable_income):
    tax = 0

    for lower, upper, rate in TAX_BRACKETS:
        if taxable_income > lower:
            # Calculate the taxable amount in the current bracket
            taxable_amount = min(taxable_income, upper) - lower
            tax += taxable_amount * rate
        else:
            break  # Stop if income is below the current bracket

    return {"Calculated Tax": tax}
