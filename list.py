# fruits = ['apple','banana','pineapple']
# print(fruits)
# number =[1,2,3,4,5]
# print(number)
# mixedList = [True,1,2,3,'Pevy',[1,2,3]]
# print(mixedList)
# x = [2,5,1]
# x.sort()
# print(x)

# # we use +ve and -ve indexing to pick elements
# print(fruits[0])
# print(fruits[-1])

# numbers = [10,20,30,40,50]                                                                      
# # print(numbers[1:])
# # print(numbers[0:3])
# # print(numbers[0:-2])

#modifying a list
# numbers = [10,20,30,40,50]      
# # numbers[0]=5
# numbers =  [5] + numbers 
# print(numbers)

#or
# numbers = [10,20,30,40,50]  
# numbers.append(5)                # it inserts an element at the end of the list
# numbers.insert(1, 5)             # it inserts an element at the second position
# print(numbers)

#Removing Items
## Removes remove  

# fruits = ['apple','banana','pineapple']

# fruits.remove('banana')
# print(fruits)

# fruits.pop(0)
# print(fruits)

# del [fruits[0]]
# print(fruits)

# fruits.clear('apple')
# print(fruits)

student = {
    "name":" Alice",
    "age": 15
 }

# print(student)
print(student["age"])
print(student.get("gender"))

student["name"]="Pevy"
print (student)
