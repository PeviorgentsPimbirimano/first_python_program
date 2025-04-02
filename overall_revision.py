#declaring variables and printing them
# name="Peviorgents Pimbirimano"  # declaring variables
# gender="Male"          #str
# Age =20                #int
# fees_paid = 100.89     #float
# registerPresent = True #bool

# print(name)            #printing variables
# print(gender)
# print(Age)
# print(fees_paid)
# print(registerPresent)

# print(type(name))              #printing the datatypes of a variable
# print(type(gender))
# print(type(Age))
# print(type(fees_paid))
# print(type(registerPresent))

# #calculations using variables
# a = 2
# b = 4
# addition = a + b
# subtraction = a - b
# multiplication = a * b
# division = a / b
# division1 = a // b            #division ,resulting in the answer being an integer
# exponent = b ** a
# exponent1 = pow(b,a)

# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)
# print(division1)
# print(exponent)
# print(exponent1)

#calling variables
#formatted strings

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

# name = "Khluivert"
# gender = "male"

# print(f"Your name is {name}  and you are a {gender}")

# gender = "male"
# if gender == "male":
#     print(f"{name} is a {gender}")
# else:
#  if gender == "female":
#     print(f"{name} is a {gender}")

# Username = "khluivert"
# Password = 406
# Username = input("Enter username ")
# Password = int(input("Enter password "))

# if  Username  == "khluivert" and Password == 406 :
#     print("Welcome admin")
# else:
#     print("Invalid username and password")
    

#  #or
# Username = "khluivert"
# Password = 406


# if  Username  ==  input("Enter username ") and Password == int(input("Enter password "))  :
#     print("Welcome admin")
# else:
#     print("Invalid username and password")

#lists
numbers = [1,2,3,4,5,6,7,8,9,10]
names = ["khluivert","Keondree","Kimberly","Khloe"]
mixedList = [False,'Pevy',1,2,3,[1,2,3]]

#modifying lists
numbers.sort()
names.sort()
print(numbers.reverse())
print(names.reverse())

#Indexing
print(numbers[0])
print(names[-1])

#slicing using indexing
print(numbers[1:])
print(numbers[0:3])
print(numbers[0:-2])

numbers = [1,2,3,4,5]      
numbers[0]=6
numbers =  [6] + numbers 
print(numbers)

#or
numbers = [1,2,3,4,5]  
numbers.append(6)                # it inserts an element at the end of the list
numbers.insert(1, 5)             # it inserts an element at the second position
print(numbers)


names = ["khluivert","Keondree","Kimberly","Khloe"]

# names.remove('kimberly')
# print(names)

# names.pop(0)
# print(names)

# del [names[0]]
# print(names)

# names.clear('khloe')
# print(names)

#tuples
# Tuples are ordered and unchangables, and much faster than Sets   

# colours = ("red","green","blue","white")

# print(colours.index("blue"))
# print(colours.count("white"))
# print(colours)

# num = (1,2,3,4,5)
# num1 = (20,10,40,30,50)
#names = ("khluivert","Keondree","Kimberly","Khloe")

#modifying a tuple
# List = list(num)
# List.extend(num1)
# print(List)
# List = tuple(num1)
# print(List)


#or#
# print(num + names)

# List = List.sort()
# print(List)

# num1 = list(num1)
# num1.sort()
# num1.reverse()
# print(num1)

#or#

# num1.sort(reverse=True)
# print(num1)


#sets
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

set = {1,2,3,4,5,6}
set1 = {6,7,8,9,10}

# unionSet = set | set1
# print(unionSet)
# interSet = set & set1
# print(interSet)
diffSet = set - set1
print(diffSet)

#or#
# unionSet = set.union(set1)
# print(unionSet)
# interSet = set.intersection(set1)
# print(interSet)
# diffSet = set.difference(set1)
# print(diffSet)

#loops
# loops used to repeat a block of code multiple times
# Two types of loops, primary types
# While loops and For loops

# While loop#
# name = input("Enter name:  ")
# while name == "":
#     print("Did not enter name")
#     name = input("Enter name:  ")
# else:
#     print(f"Your name is {name}")

# i = 0
# while i <=10:
#     print(i)
#     i = i + 1

# n = 7
# number = int(input("Enter your guess:  "))
# while number != n :
#      print("Wrong guess")
#      number = int(input("Enter your guess:  "))   
# else:
#      print("Correct guess!")
         
# n = 8
# print("WELCOME TO GUESS THE NUMBER")

# number = int(input("Enter your guess:  "))
# while n != number:

#     print("Wrong guess!")
    
#     if number > n :
#         print("HINT: Your is greater than the correct number!")
    
#     if number < n :
#         print("HINT: Your number is less than the correct number!")
#     number = int(input("Enter your guess again:  "))

# else:
#     print("Correct guess!")

# b = "q"
# back = (input(" Do you want to exit press (q), if not click ENTER:"))
# guess = int(input("Enter your guess:  "))
# while True:
#     if guess > 8:
#         print("HINT: Your number is greater than the correct number!")
#         guess = int(input("Enter your guess:  "))
#     elif guess < 8:
#         print("HINT: Your number is lesser than the correct number!")
#         guess = int(input("Enter your guess:  "))
#     elif back==b:
#         quit
    
#     else :
#         print("Correct guess!")
#         back = (input(" Do you want to exit press (q):"))
#             #  back = (input(""))

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

#or#
# i = 1
# while i <= 10 and i > 0:
#     print(i)
#     i = i + 1
    
# i = 10
# while i <= 10 and i > 0:
#     print(i)
#     i = i - 1   
# number = [1,2,3,4,5,6,7,8,9,10]

# n = int(input("Enter a number:  "))
# if n % 2 == 0 :
#     print("Even")
# else:
#     print("Odd")
       
#For loops are used to iterate over a sequence (list, tuples, dict, strings)

# for x in colours:
#     print(x)
# print()

# for x in colours:
#     for y in colours:
#       print(y, end="  ")
# print()

# for x in colours:
#     for y in colours:
#       print(y, end=" \n ")
# print()

# print(len(colours))
# print(dir(colours))
# print("red" in colours)
# print(sorted(colours))
# print(colours)

# fruits = ["apple", "banana", "pineapple" ]
# for fruit in fruits:
#     print(fruit)

#      #LOOPING THROUGH A STRING#
# txt = "Keondree"
# for char in txt:
#     print(char)

#dictionaries
classroom ={
    "name":"khluivert",
    "gender":"male",
    "class": 8,

}


student = {
    "name":" Alice",
    "age": 15
 }

# print(student) and modifying a dictionary
print(student["age"])
print(student.get("gender"))

student["name"]="Pevy"
print (student)


#functions
# Function is a block of code which can be reused
# def newYear (Year, x):
#     print("Happy new year")
#     print(f"Welcome to {Year}")
#     print(f"Your {x} year")
#     print()

# newYear(2026, "18^th")
# newYear(2027, "19^th")
# newYear(2028, "20^th")
# newYear(2029, "21^st")

  #adding strings
# def add(name,last):
#     fullname = name + last
#     return fullname

# print(add("Pevior","gents"))
 
    #adding int
# def add(x,y):
#     z = x + y
#     return z

# print( add(2,5))

# num = int(input("Enter number: "))
# while True:
#     if num % 2 ==0:
#         print("even number")
#     num = int(input("Enter number: "))
# else:
    
#     print("odd number")
#     num = int(input("Enter number: "))


# def power(num,exponent):
#     return num**exponent

# print(power(2,3))
  #or#
# def multiply(a,b):
#     return a * b
# result = multiply(2,4)
# print(result)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

# def Name(name="Pevy"):
#     print(f"Your name is {name}")
# Name()


def zim():
    print("This is zimbabwe")
zim() 

def Bul():
    zim()
    print("This is bulawayo")
Bul()
def hr():
        zim()
        print("This is harare")
hr()

#file handling

# with open("index.txt","a") as file:
#     file.write("""\nHello Pevy
# How are you
# TYU
# QWE
# RGF
               
# """)

# write_file = open(r"C:\Users\Perviorgents Pambiri\Documents\Fakefile.txt","w")
# write_file.write("This is our first sentence in our file ")
# write_file.close()


# Append_file = open(r"C:\Users\Perviorgents Pambiri\Documents\Fakefile.txt","a")
# Append_file.write(" This is our second sentence in our file")
# Append_file.close()

# #context manager#
# with open(r"C:\Users\Perviorgents Pambiri\Documents\Fakefile.txt","a") as Append_file:
#     Append_file.write(" This is our third sentence in our file")
#     Append_file.write(" \nThis is our fourth sentence on an another line in our file")


# #reading the context manager#
# with open(r"C:\Users\Perviorgents Pambiri\Documents\Fakefile.txt","r") as Read_file:
#     print(Read_file.read())

#   #Appending multiple lines#
# Multi_lines = """
# This is our fifth sentence on an another line in our file
# This is our seventh sentence on an another line in our file
# This is our eighth sentence on an another line in our file`
# """

# with open(r"C:\Users\Perviorgents Pambiri\Documents\Fakefile.txt","a") as Append_file:
#     Append_file.write(Multi_lines)

# with open(r"C:\Users\Perviorgents Pambiri\Documents\Fakefile.txt","r") as Read_file:
#     print(Read_file.read())

##method 2 of: creating (x)
#               reading (r)
#               writing (w)
#               appending (a)

f = open("Fake_file.txt","r")
# print(f.read())
# print(f.read(4))       #prints the first four letters 
# print(f.readline())
#print(f.readlines())

for line in f:
    print(line)
f.close()

try:
    f = open(" Try_file.txt")
    print(f.read())
except:
    print("The file doesn't exist")
finally:
    f.close()

print("Hello world")