


print("Hello!\n Welcome to the Age Teller!")
name = input("What is your name?\n")
age = input("And how old are you today?\n")
year = 2016
year_100 = (100 - int(age)) + (year - 1)
print("{}, you will turn 100 in the year {}!".format(name, year_100))
