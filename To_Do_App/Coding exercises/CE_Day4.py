# Coding Exercise 1
# Create a program that:
#
# 1. Prompts the user to input a (dollar) amount.
# 2. Calculates the corresponding amount in euros, given an exchange rate of 2.
# 3. Prints out the amount in euros.

rate = 2

amount = float(input("Enter an amount: "))

exchange = amount * rate
print(exchange)

# Coding Exercise 2
# The ranking list given in the coding area represents the ranking of three athletes, John, Sen, and Lisa. John won 1st place, Sen got 2nd, and Lisa 3rd.
#
# Your task is to create a program that:
#
# 1. Contains the above list.
# 2. Prompts the user to input a rank number.
# 3. Returns the person who has the given rank.

ranking = ['John', 'Sen', 'Lisa']

choice = int(input("Enter rank number: "))
print(ranking[choice-1])

# Coding Exercise 3
# We have defined the same ranking list as in the previous exercise:
#
# This time you should create a program that:
#
# 1. Contains the above list.
# 2 Prompts the user to input the person's name.
# 3. Returns the rank that person has.

ranking = ['John', 'Sen', 'Lisa']

name = input("Enter a name: ")

match name:
    case 'John':
        print("1")
    case 'Sen':
        print("2")
    case 'Lisa':
        print("3")

# Coding Exercise 4
# Create three variables mood, strength, and rank and assign a string to mood,
# a float to strength, and an integer to rank. The values you assign can be anything as long as they are of the correct type.

mood = 'BAD'
strength = 1.5
rank = 1

#
# Coding Exercise 5
# Create a color_codes variable and assign a tuple to it.
#
# The tuple should contain three tuples as items. Each of the three tuples should contain three items. The items can be any type.

color_codes = ((1,2,3),(4,5,6),(7,8,9))