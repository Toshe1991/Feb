# user_data = ("Toshe", "Petrovski", "toshe112", "abvg1234")

# user_data = {
#     "first_name": "Toshe",
#     "last_name": "Petrovski",
#     "username": "toshe112",
#     "password": "abvg1234"
# }

# user_data["phone"] = "+389785555666"
# # user_data["username"] = "toshe54321"
# print(user_data)
# print(user_data["username"])

# print(user_data)
# print(len(user_data))

# print(user_data["address"])

# .get(arg1 required, arg2 optional)

# print(user_data.get("address", "Partizanska"))

# .pop(arg1, arg2)
# password = user_data.pop("password")
# print(password)


# for item in user_data:
    # print(user_data[item])

# access certain value based on key
# print(user_data.get("address", "Partizanska"))

# .pop(<<key>>) -> to remove an element from dictionary
# my_name = user_data.pop("address", "Partizanska")
# print(f"My name is: {my_name}")
# print(user_data)

# .keys() -> list of all dictionary keys
# print(user_data.keys())

# .values() -> list of all dictionary values
# print(user_data.values())


# for item in user_data:
#     print(item + " -- " + user_data[item])

# .items() -> list of tuples with all key:value pairs [(key, value), (key, value)]
# for key, value in user_data.items():
#     # key, value = item
#     print(key, value)
    # print(item)

user_data = {
    "first_name": "Toshe",
    "last_name": "Petrovski",
    "username": "toshe112",
    "password": "abvg1234",
}

user_data2 = {
    "Address": "Partizanska",
    "phone": "012345"
}

# .update(<<arg>>) -> merge between two dictionaries
# user_data.update(user_data2)
# print(user_data)

# .clear() -> if you want to delete all elements from dictionary
user_data.clear()
print(user_data)






