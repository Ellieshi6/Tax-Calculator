from income import get_income, taxable_income

# loop that prints out user's input, and only continues if all entered information is correct
while True: 
  user_data = get_income()
  print('\n')
  for key, value in user_data.items():
    if isinstance(value, float):  # Add $ only for float values
      print(f"{key}: ${value:.2f}")
    else:
      print(f"{key}: {value}")

  confirmation = input("\nPlease confirm that this is correct (y/n): ")

  while (confirmation != 'y') or (confirmation != 'n'):
    if confirmation == 'y':
      print("\nyay! continuing...\n")
      break
    elif confirmation == 'n':
      print("\noopsies let's fix that\n")
      break
    else:
      print("\nInvalid input, please enter 'y' or 'n'.\n")

    confirmation = input("Please confirm that this is correct (y/n): ")
  if confirmation == 'y':
    break


taxable_income = taxable_income(user_data)
for key, value in taxable_income.items():
  print(f"{key}: ${value:.2f}")