# Author: Toan Le
# Email: tle153@student.gsu.edu
# Assignment: Lab 7
# Date: 10/05/2022
'''
o Purpose: offer the user a choice of food items, calculate total bill
o
Pre-conditions: user enters 5 or 6 y's or n's depending on desired items
(strings)
o
Post-conditions: prompts for choices, total bill before (float) and after
tip, (float)
o and parting message.
o '''
# name of restaurant
# give user instructions of expected inputs
# initialize total bill to zero
# ask first choice
# if the user desired the item,
#add price to total bill

# output blank line
# output total bill before tip

# create array and set price for each item on the menu
menu_price = [7.0, 5.0, 8.0, 8.0, 2.0, 6.0]
# create array and store names of each item
menu_arr = [
  'a grilled cheese', 'a serving of nachos', 'chicken sandwich', 'hamburger', 'cheese on that', 'hot dog'
]

def main():
  # introductory message with name of restaurant
  print('Welcome to Dairy King')

  # instructions for user input
  print('Please answer each question with y or n')

  # create new variable for total cost and set value at 0
  total_bill = 0

  # prompt for user input for grilled cheese, nachos, and chicken sandwich
  for i in range(3):
    food = input("Do you want " + str(menu_arr[i]) +'? ')

    # add cost to total bill if user enters 'y'
    if food == 'y':
      total_bill += menu_price[i] + 0.0

  # prompt for user input for hamburger
  hamburger_check = input("Do you want a Hamburger? ")

  # if user enters 'y' for burger, add cost to total bill
  if hamburger_check == 'y':
    total_bill += menu_price[3]
    # ask if they want to add cheese, if yes, add cost to total bill
    if input('Do you want cheese on that? ') == 'y':
      total_bill +=menu_price[4]

  # prompt for user input for hot dog, if yes, add cost to total_bill
  if input('Do you want a hot dog? ') == 'y':
    total_bill += menu_price[5]

  # create new variable and add 20% tax to get total after tax
  total_with_tax = total_bill * 1.2

  # output cost before tax with 2 decimals
  print("The total for your food is $" + str(format(total_bill, '.2f')))

  # output cost after tax
  print(f'The total with 20% tip is ${total_with_tax:.2f}')
  print('Thank you for your business!')

main()