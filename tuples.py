# fruits = ("apples", "oranges", "bananas")
# print(id(fruits))
# # print(fruits[1:3])
# # print(type(fruits))
#
# vegetables = ("cucumber",)
# # print(type(vegetables))
#
# # fruits_tuple = tuple(fruits)
# # print(type(fruits_tuple))
#
# fruits += ("strawberries",)
# print(id(fruits))
# print(fruits)

# fruits = {"apples", "oranges", "bananas"} -> 0001, 0002, 0003, 0004, 0005

# "apples" in fruits

# f("apples") -> 0001

# md5 ("apples") -> "0001" # hash collisions

# tuple packing
# fruits = ("apples", "oranges", "bananas")
# credentials = ("someusername", "somepassword")
#
# username, password = credentials
#
# # tuple unpacking
# fruit1, fruit2, fruit3 = ("apples", "oranges", "bananas")
# print(fruit1)
# print(fruit2)
# print(fruit3)

# a = 10
# b = 20
#
# temp = a
#
# a = b
# b = temp
#
# print(f"a: {a}, b: {b}")
a = 10
b = 20

a, b = (b, a)  # -> (0001 -> 20, 0002 -> 10)

print(f"a: {a}, b: {b}")







