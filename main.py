import random


random_number = random.randint(0,1)
print(random_number)
if random_number == 0:
    print('Tails')
else:
    print('Heads')


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name_length = len(names)
random_number = random.randint(0, name_length - 1)
print(f'{names[random_number]} is going to buy the meal today!')


# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "🙂"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
map_data = [rock, paper, scissors]

print(f'user choice: {user_choice}, computer choice: {computer_choice}')
print('User choice is \n' + map_data[user_choice])
print('Computer choice is \n' + map_data[computer_choice])

if user_choice == computer_choice:
    print("It's a draw.")
elif ((user_choice == 0 and computer_choice == 2) or
      (user_choice == 1 and computer_choice == 0) or
      (user_choice == 2 and computer_choice == 1)):
    print("You win.")
elif ((user_choice == 0 and computer_choice == 1) or
      (user_choice == 1 and computer_choice == 2) or
      (user_choice == 2 and computer_choice == 0)):
    print("You lose.")
