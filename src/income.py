# retrieves user's basic income streams
def get_income():
  week_salary = float(input("Please enter your estimated weekly income from wages alone: "))
  week_salary_weeks = int(input("How many weeks per year do you expect to receive this income? : "))
  month_investment_income = float(input("Please enter your estimated monthly investment income; i.e. from property, shares, art: "))
  month_investment_month = int(input("For how many months of the year do you expect to receive this investment income? : "))
  return {
    "Weekly Salary": week_salary,
    "Estimated Working Weeks": week_salary_weeks,
    "Monthly Investment Income": month_investment_income,
    "Estimated Months of Investment Income": month_investment_month
  }

# calculates user's taxable income using user_data
def taxable_income(user_data):
  week_salary = user_data["Weekly Salary"]
  week_salary_weeks = user_data["Estimated Working Weeks"]
  month_investment_income = user_data["Monthly Investment Income"]
  month_investment_month = user_data["Estimated Months of Investment Income"]
  total_taxable_income = (week_salary * week_salary_weeks) + (month_investment_income * month_investment_month)
  return {"Annual Total Taxable Income": total_taxable_income}

