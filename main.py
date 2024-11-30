import random

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

student_total = 0
student_count = 0
#Write your code below this row 👇
for student_height in student_heights:
    student_total += student_height
    student_count += 1

student_average = round(student_total / student_count)
print(student_heights, student_average)


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
highest_score = student_scores[0]
lowest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

print(f'The highest score in the class is: {highest_score}, and the lowest score is: {lowest_score}')

total = 0
for number in range(2, 101, 2):
    print(number)
    total += number
    # if number % 2 == 0:
    #     print(number)
    #     total += number

print(total)


for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)


# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

eazy = ''
for i in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    eazy += random_letters

for j in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    eazy += random_symbols

for k in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    eazy += random_numbers

print(eazy)

characters = []
for i in range(1, nr_letters + 1):
    characters.append(random.choice(letters))

for j in range(1, nr_symbols + 1):
    characters.append(random.choice(symbols))

for k in range(1, nr_numbers + 1):
    characters.append(random.choice(numbers))
random.shuffle(characters)

hard = ''
for i in characters:
    hard += i
print(hard)