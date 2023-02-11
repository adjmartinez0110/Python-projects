#creating atm to withdraw money using user defined function

def withdrawal(amount):

  balance = 500
  
  
  if amount > balance:
    print()
    print("Error: your account balance is too low. Please enter another amount.")

  else:
    print()
    print("Here is your money. Thank you for using our service.")
    balance = balance - amount

    print()
    print("Your current balance is now " + str(balance) + ".")

money_withdraw = int(input("Please enter amount to withdraw: "))
withdrawal(money_withdraw)
    