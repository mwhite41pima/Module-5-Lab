# Marquies White
# 10/6/2024
# Lab 5: The Bottle Return Program
# This program takes the number of bottles returned over a certain number of days 
# and calculates how much money was paid out to whomever returned the bottles

# Declaring variables
total_bottles = 0
today_bottles = 0
total_payout = 0
keep_going = "y"

# Payout amount per bottle
payout_per_bottle = 0.10

# Number of days in a week
nbr_of_days = 7

# Loop to gather amount of bottles and payout
while keep_going == "y":
    total_bottles = 0
    counter = 1

    while counter <= nbr_of_days:
        today_bottles = int(input(f"Enter the number of bottles returned for day #{counter}:"))
        total_bottles = total_bottles + today_bottles
        counter = counter + 1

    total_payout = total_bottles * payout_per_bottle        
    print("Total number of bottles returned:", total_bottles)
    print("Total payout: $", total_payout)

    keep_going = input("Do you want to enter another week of bottles? (y/n)")