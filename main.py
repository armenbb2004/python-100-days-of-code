# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(two_digit_number[0]) + int(two_digit_number[1]))


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight/height**2)
print(bmi)


# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_remaining = 90 - age

year_day = 365
year_weeks = 52
year_month = 12

days_spent = years_remaining * year_day
weeks_spent = years_remaining * year_weeks
months_spent = years_remaining * year_month
print(f'You have {days_spent} days, {weeks_spent} weeks, and {months_spent} months left.')

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places.
print('Welcome to tip calculator.')
bill = float(input('What was the total bill? $'))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

full_price = bill + bill * percentage / 100
each_person = full_price / people

print('Each person should pay ${:.2f}'.format(each_person))
