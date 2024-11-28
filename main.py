# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 1:
    print('This is an odd number.')
else:
    print('This is an even number.')

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / height ** 2)

message = f"Your bmi is {bmi}, you are "
if bmi < 18.5:
    print(message + "underweight.")
elif bmi < 25:
    print(message + "normal weight.")
elif bmi < 30:
    print(message + "overweight.")
elif bmi < 35:
    print(message + "obese.")
else:
    print(message + "clinically obese.")


# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not leap year')
    else:
        print('Leap year')
else:
    print('Not leap year')

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f'Your bill is: ${bill}')


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name_lower = (name1 + name2).lower()

t = name_lower.count('t')
r = name_lower.count('r')
u = name_lower.count('u')
e = name_lower.count('e')

true = t + r + u + e

l = name_lower.count('l')
o = name_lower.count('o')
v = name_lower.count('v')
e = name_lower.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
choice = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if choice == 'left':
    choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice == 'wait':
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice == 'yellow':
            print("You found the treasure! You Win!")
        elif choice == 'red':
            print("It's a room full of fire. Game Over.")
        elif choice == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
