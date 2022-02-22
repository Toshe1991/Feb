# VOID Functions

def print_hello_message(name):
    print(f"Hello {name} from the course")

# print_hello_message("Toshe")
# print_hello_message("Vladimir")
# print_hello_message("Kristijan")


# # value returning functions
# def my_sum(num1, num2):
#     return num1 + num2
#
# num_sum = my_sum(5, 15)
# print(num_sum)

# Global scope
# name = "Toshe"
#
# def print_my_name(welcome_message):
#     # local scope -> variables defined here are local to this function
#     name = "Toshe"
#     print(name)
#     print(welcome_message)

# numbers = [5, 10, 15, 20, 25] # -> 0001
# my_sum = 10 # -> 0002
#
# # in Python all arguments are passed by reference
# def mutate_value(num):
#     # num -> 0002
#     num = 5
#     # my_numbers -> 0001
#     # my_numbers.append(100)
#
# mutate_value(my_sum)
# print(my_sum)
# print(numbers)
# def calculate_list_sum(numbers_collection):
#     global my_sum
#     my_sum = 0
#     for number in numbers_collection:
#         my_sum += number
#
#     return my_sum
#
# # total = calculate_list_sum(numbers)
# # print(total)
# print(my_sum)

# Positional arguments
def my_sum(num1, num2, num3, num4, num5):
    return num1 + num2

# num_sum = my_sum(5, 15, 20, 25, 30)


# # keyword arguments
# def generate_username(first_name, last_name, country="Macedonia", location=None):
#     if not location:
#         location = []
#     # location.append("Karpos")
#     # print("Location is ", location)
#     username = first_name.lower() + last_name.lower() + country.lower()
#     return username
# #
# my_username = generate_username(last_name="Petrovski", first_name="Toshe", location=["Partizanska", "Skopje"])
#
# username2 = generate_username(first_name="Gjoko", last_name="Vladev")
# # print(my_username)


# def test_function(num1, num2, *args):
#     # print(list(args))
#     print(num1)
#     print(num2)
#     total = 1
#     for number in args:
#         total *= number
#     print(total)
#
# test_function(2, 4, 6, 8, 10, 12)


# def generate_username(first_name, last_name, country="Macedonia", **kwargs):
#     # location.append("Karpos")
#     # print("Location is ", location)
#     print(kwargs)
#     username = first_name.lower() + last_name.lower() + country.lower()
#     return username
#
# generate_username(first_name="Toshe", last_name="Petrovski", phone="12345", profession="developer")

# !10 -> 10 * 9 * 8 ... 1

def calculate_factorial(num):
    """
    Return the factorial of the given parameter num.

    :param num: arbitrary integer
    :return: the factorial calculated
    """
    if num == 1:
        return 1

    return num * calculate_factorial(num-1)
#
# print(calculate_factorial(4))

calculate_factorial()





