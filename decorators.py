def test():
    print("In Test Function")

a = 10 # -> 0001 -> 10

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

def get_test_func():
    return test  # return the reference to test function

def parent_func():
    def child_func():
        print("IN CHILD FUNC")

    child_func()
    child_func()


parent_func()
# b = get_test_func()
#
# print(id(b))
# print(id(test))
#
# print(b())
