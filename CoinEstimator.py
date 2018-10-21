'''

Coin Estimator By Weight
When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill up the container, they’ll roll them up in coin wrappers which can then be traded in at a bank for what they are worth. While most banks will give away coin wrappers for free, it’s convenient to have an idea of how many you will need. Instead of counting how many coins you have, it’s easier to separate all of your coins, weigh them, and then estimate how many of each type you have and then how many wrappers you’ll need. For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.

Here is the weight of each coin and how many fit inside each type of wrapper.

Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all of their money.
Subgoals:
Round all numbers printed out to the nearest whole number.
Allow the user to select whether they want to submit the weight in either grams or pounds.
'''

from math import ceil

print("Hi there! You have to input total weight for each type of coins (pennies, nickels, dimes, and quarters)")

pennies_weight=float(input("Input approx. weight for pennies"))
nickels_weight=float(input("Input approx. weight for nickels"))
dimes_weight=float(input("Input approx. weight for dimes"))
quarters_weight=float(input("Input approx. weight for quarters"))

total_pennies=int(pennies_weight/2.5)
total_nickels=int(nickels_weight/5)
total_dimes=int(dimes_weight/2.20)
total_quarters=int(quarters_weight/5.6)

# weightUnit = input("Do you use grams or pounds? g/lb")

print('''
1 penny weighs 2.5 gms
1 nickle weighs 5 gms
1 dime weighs 2.20 gms
1 quarter weighs 5.6 gms
''')

print('''You have
 {} pennies, {} nickels, {} dimes, {} quarters
'''.format(total_pennies,total_nickels,total_dimes,total_quarters))

input("press enter to proceed")

print("Number of each coin contained  per roll.")
print('''
penny = 50,
nickle = 40
dime = 50
quarter = 40

''')

penny_rolls=ceil(int(total_pennies/50))
nickle_rolls=ceil(int(total_nickels/40))
dime_rolls=ceil(int(total_dimes/50))
quarter_rolls=ceil(int(total_quarters/40))

total_rolls=penny_rolls+nickle_rolls+dime_rolls+quarter_rolls


print('''You need {} rolls for pennies, {} rolls for nickles, {} rolls for dimes and {} rolls for quarters
Total rolls needed = {}
'''.format(penny_rolls,nickle_rolls,dime_rolls,quarter_rolls,total_rolls))
