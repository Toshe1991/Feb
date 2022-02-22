a = 10

b = -10.5

# immutable types collection
# name = "Toshe"
# print(id(name))
# id() -> return memory address of the object value

# name = "Vlatko"
# print(id(name))
#
# # Dealocation of memory
# del name

# print(name[])

# for char in name:
#     print(char, end="--")

# counter = 0
# while counter < 5:
#     print(name[counter])
#     counter += 1

# surname = "Petrovski"
#
# name = input("Please enter your name: ")
#
# print(name)

"""
This is a comment.
This is another comment.
"""

# In Python we dont use ; to set end of line.
# IN Python we don't use brackets to signify block of code, replacement for brackets is indentiation


# STRINGS
# \ se narekuva escape character
# \n newline character

name = "I wasn't there, my name is \"Toshe\""

sentence = '''
Hello my name is 'toshe.
I am from Skopje
We are learning Python
'''

# + operatorot pomegju stringovi se korsti za konkatenacija

# sentence = "Hello my name is toshe \n" + \
#         "I am from skopje"

# print("Hello my name is Toshe")

# len() -> korstime za da proverime dolzina na string

# name = "Toshe"
#
# print(len(name))

sentence = "Hi, my age is 29"

# in operatorot go korstime za da proverime substring

# print("29." in sentence)

# not prefiksot go dodavame za da ja promenime evaluiranta vrednost

# age = input("Please enter your age: ")
#
# print("18" not in age)

# slicing - extracting substring from the string

sentence = " Hello from #:785439785743 Python course -"

# [] for indexing can get up to 3 arguments, arguments are divided using :
# [start:stop:step], stop and step are optional, stop index is not inclusive

# print(sentence[::-1])

# For more complex pattern matching in text we use REGULAR EXPRESSIONS

# .find() -> 1 argument, substring to search for
#
# start_position = sentence.find("#:", 20)
# print(start_position)
# print(sentence[start_position+2:start_position+5])

# print(sentence.upper())
# print(sentence.lower())

# print(sentence.strip("-"))

# print(message.replace("name", input_name))

# C-Style string  formatting

# message = "Good morning, Mr. %s, you are in %s" % (input_name, place)
# print(message)

# .format()
# sentence = "Good morning, Mr. {name}, you are in {city}".format(city=place, name=input_name)
# print(sentence)

# f - string formatting

# sentence = f"Good morning, Mr. {input_name}, you are in {place}"
# print(sentence)

# input_name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))

# If and else and mutually exclusive
# n > 20 and n < 25 -> chain expression
# 20 < n < 25

# if age < 18:
#     print("You are still a minor, can't buy alcohol")
# elif age >= 18 and age <= 21:
#     have_adult = input("Do you have an adult with you: ")
#     if have_adult.lower() == "yes":
#         print("You can buy alcohol")
#     else:
#         print("You can't buy alcohol, must have adult with you")
# else:
#     print("You can buy alcohol")
#
#

# Short hand if-else, Ternary operations or Conditional Expressions

a = 10
b = 20

# if a < b:
#     print("A is lower than b")


# if a < b: print("A is lower than b"); print("Second statement")


# Conditional assignment

age = 15

# if age < 18:
#     age_string = "minor"
# else:
#     age_string = "adult"
#
# age_string = "minor" if age < 18 else "adult"
#
# print("Hello from me") if age < 18 else print("Hello again")

# surname = input("Please enter your surname: ")
# class_name = None
#
# if surname[0] == "A":
#     class_name = "4a"
# elif surname[0] == "B":
#     class_name = "4b"
# elif surname[0].isdigit():
#     pass  # {}
# elif surname[0] == "C":
#     class_name = "4c"
# else:
#     class_name = "4d"
#
#
# print(class_name)
#
#


# a = ""
# print(type(None))


# a = 10
# a -> STACK(0001) [0002] -> HEAP()[10]

# id() -> memory address of the object
# a = 10
# print(id(a))


# we can compare objects by value or by reference

# a = int(input("Enter value: "))
# b = int(input("Enter value: "))


a = None

if a is None:
    print("A is None")



































