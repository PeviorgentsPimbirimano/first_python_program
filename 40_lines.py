 # Sets ia a collection of unorderable items and does not allow duplication

# colours = {"red","green","blue","white"}

# print(colours)
# print(len(colours))
# print("red" in colours)
# print("black" in colours)

# colours.add("black")
# print(colours)
# colours.remove("white")
# print(colours)

# for x in colours:
#     print(x)
# print()

# for x in colours:
#     for y in colours:
#       print(y, end="  ")
# print()

# Tuples are ordered and unchangables, and much faster than Sets   

# colours = ("red","green","blue","white")

# print(colours.index("blue"))
# print(colours.count("white"))
# print(colours)

# for x in colours:
#     for y in colours:
#       print(y, end=" \n ")
# print()

# print(len(colours))
# print(dir(colours))
# print("red" in colours)
# print(sorted(colours))
# print(colours)

# birthYr = int(input("Enter your birth year: "))
# currentYr = int(input("Enter current year: "))

# yourAge = currentYr - birthYr
# print(f"You are aged {yourAge} years old")

# print(type(yourAge))

# if yourAge >= 18:
#     print(f"You are an adult and your age is {yourAge} ")
# else:
#     print(f"You are NOT an adult and you are aged {yourAge}")


# Gender = input("Enter your gender(male/female):  ")
# second_Gender = input("Enter you patners' gender(male/female):  ")

# if Gender == "male" and second_Gender == "male":
#     print("You are GAY but WHY are you gay")
# else:
#     print("Chane babe")

# Temp = int(input("Enter the environments' degrees:  "))
# Condition = input("Enter the environment's condition(SUNNY/CLOUDY):  ")

# if Temp >= 30 and Condition == "SUNNY":
#     print(f"It is a {Condition} day and your degrees are {Temp}")
# else:
#     print(f"THE WHEATHER IS COLD      (It is a {Condition} day and your degrees are {Temp})")
  
# day = "monday"
# print(day.lower())
# print(day.upper())

# day = input('Enter day:  ').lower()

# if day == "monday":
#     print("Wear formal")
# elif day == "tuesday":
#     print("Wear casual")
# elif day == "wednesday":
#     print("Wear ripped jeans")
# elif day == "thursday":
#     print("Wear simple clothings")
# elif day == "friday":
#     print("Wear formal")
# else:
#     print("It is not a working day ")

# score = int(input("Enter your score:"))

# if score >= 90 and score <= 100:
#     print("Grade is: A")
# elif score >= 80 and score < 90:
#     print("Grade is: B")
# elif score >= 70 and score < 79:
#     print("Grade is: C")
# elif score >= 60 and score < 69:
#     print("Grade is: D")
# elif score <= 60 and score>= 0 :
#     print("Grade is: F")
# elif score <=-1 :
#     print("Score is invalid")
# elif score>=101 :
#     print("Score is invalid")
# else:
#     print("Score is invalid")


# number = [1,2,3,4,5,6,7,8,9,10]

# n = int(input("Enter a number:  "))
# if n % 2 == 0 :
#     print("Even")
# else:
#     print("Odd")