#determining whether a number is prime or not
import math

num = int(input("Please enter a number: "))


if num < 3:
  print("Error")

for i in range(2, int(math.sqrt(num) + 1)):
  if num % i == 0:
    print(str(i) + ": factor") #if this shows up just once, the number is not prime
    
  else:
    print(str(i) + ": not a factor")
    


#Algorithm
# 1. Import math statement
# 2. Enter the number/ask user input
# 3. Error check: check for positive numbers
# 4. use for loop to go through numbers up to selected number (square root)
# 5. if statement to determine whether prime or not (with factors)