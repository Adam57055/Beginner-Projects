# coin weight in grams
pennyWeight = 2.5
nickelWeight = 5.0
dimeWeight = 2.268
quarterWeight = 5.670

# amount of coins that fit in each type of wrapper
pennyWrapper = 50
nickelWrapper = 40
dimeWrapper = 50
quarterWrapper = 40
#weight is estimated by amount of coins in a wrapper
print("Welcome to the Coin Estimator!")
print("Please enter the weight of your: ")

pennies = float(input("Pennies: "))
nickels = float(input("Nickels:" ))
dimes = float(input("Dimes: "))
quarters = float(input("Quarters: "))

#amount of coins by the information user inputs
penny_amount = pennies * pennyWeight
nickel_amount = nickels * nickelWeight
dime_amount = dimes * dimeWeight
quarter_amount = quarters * quarterWeight

#Print results
print(penny_amount)
print(nickel_amount)
print(dime_amount)
print(quarter_amount)
