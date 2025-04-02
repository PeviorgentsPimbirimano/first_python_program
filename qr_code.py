
# file = open("index.txt","r")
# content = file.read()
# print(content)

# file.close()

# with open("index.txt","r") as file :
#     content = file.read()
#     print (content)

# with open("index.txt","a") as file:
#     file.write("""\nHello Pevy
# How are you
# TYU
# QWE
# RGF
               
# """)


# import os
# if os.path.exists("index.txt"):
#     os.remove("index.txt")


#     print("file exists")
# else:
#     print("file doesn't exists")


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