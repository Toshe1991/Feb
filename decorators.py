# def test():
#     print("In Test Function")
#
# a = 10 # -> 0001 -> 10

# b = test
#
# b()
# test()

# print(id(test))
# print(id(b))
# print(type(b))

# def call_inner_function(func):
#     print("In outer function")
#     func()
#
# call_inner_function(test)

# def get_test_func():
#     return test  # return the reference to test function

def parent_func():
    def child_func():
        print("IN CHILD FUNC")

    child_func()
    child_func()


# parent_func()
# b = get_test_func()
#
# print(id(b))
# print(id(test))
#
# print(b())


# decorator or wrapper
# def print_before_exec(func):
#     print("Before running inner function")
#     func()
#
#
# def hello_message():
#     print("Hello Semos Course")
#
#
# print_before_exec(hello_message)
#

# decorator
# def message_decorator(func):
#     # local scope -> objects are created when function is called
#     def inner():
#         print("Before execution of func")
#         func() # -> original function_to_be_used // 0001
#         print("After execution of func")
#
#     return inner
#     # object are destroyed when function exists
#
#
# def function_to_be_used():
#     # we want to execute smt else here
#     print("This is inside function to be used")
#     # we want to execute smt else here
#
#
# def function_to_be_used2():
#     # we want to execute smt else here
#     print("This is inside function2 to be used")
    # we want to execute smt else here
# 1. definiriame message_decorator
# 2. definirame function_to_be_used
# 3. redefine function_to_be_used variable to be return from message_decorator
# 3.1 (right side of assignment) -> first var: func = function_to_be_used, second var: def inner
# 3.2 (right side of assignment) -> return reference to inner function (inner function)
# 3.3 (left side of assignment) -> function_to_be_used = inner


# function_to_be_used = message_decorator(function_to_be_used)
# function_to_be_used2 = message_decorator(function_to_be_used2)
# # -> 0002
# # function_to_be_used = inner
#
# function_to_be_used()
# function_to_be_used2()
#

# create decorator to make specific functions error prone
@property
def handle_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            print(f"Exception happened while calling wrapped function. Exception: {exc}")
            print("Continuing with program execution...")

    return inner


@handle_error
def test_func():
    raise Exception("Invalid data read from file.json")


@handle_error
def get_user_name():
    name = input("Please enter your name: ")
    return name


@handle_error
def divide_values(x, y, name=None):
    print(name)
    return x / y

# print(get_user_name())
# a = divide_values(10, 0, name="Toshe")
# print(a)

# def test(*args, **kwargs):
#
#     def test2(a, b, c):
#         print(a, b, c)
#
#     test2(**kwargs)
#
# test(a=10, b=20, c=30)
# test_func()
# value = divide_values(10, 0)
# print(value)
# test_func = handle_error(test_func)

# test_func()
#
# my_name = get_user_name()
# print(f"My name is: {my_name}")
# print("FINSISHED")


class Request:
    def __init__(self, url, user_id, parameters):
        self.url = url
        self.user_id = user_id
        self.parameters = parameters


def log_http(func):
    def inner(request):
        url = request.url
        print(f"Called endpoint: {url}, User: {request.user_id}, with parameters: {request.parameters}")
        response = func(request)
        print(f"Received response from {url}: {response}")

    return inner


# https://example.com/user?search=ABV&sort=id
# https://example.com/blog?title=Python&author=toshe

r1 = Request(url="https://example.com/user", user_id=1, parameters={"search": "ABV", "sort": "id"})
r2 = Request(url="https://example.com/blog", user_id=1, parameters={"title": "Python", "author": "toshe"})

@log_http
def get_user(request):
    print("Getting user from database")
    return {"status": 200, "content": "Got user 2"}

@log_http
def get_blogs(request):
    print("Getting blogs from database")
    return {"status": 200, "content": "Got blog 10"}


get_user(r1)
get_blogs(r2)












