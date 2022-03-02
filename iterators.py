# l = [10, 20, 30]
#
#
# # l -> 0001 (HEAD OF the LIST) -> 1st EL (1111) -> 2nd EL (2222) -> 3rd EL (3333)
#
# # l -> 3 elements , only gets elements ony by one when needed
#
# for i in l:
#     print(i)
l = [10, 20, 30]

# print("__iter__" in dir(l))

# iterable_list = iter(l)
#
# # print(iterable_list)
# print(next(iterable_list))
# ##########
# print(next(iterable_list))
# ##########
# print(next(iterable_list))
# ##########
# print(next(iterable_list))
# print(iterable_list.__next__())

# range(start, stop, step) -> return sequence of numbers between start and stop, with step value

# for n in range(0, 1000000000):
#     print(n)
#     if n == 500:
#         break

# num_range = range(0, 100)
# print(num_range)
# print(type(num_range))
# # print("__iter__" in num_range)

class MyRange:
    def __init__(self, start_num, stop_num, step=1):
        self.start_num = start_num
        self.stop_num = stop_num
        self.step = step
        self.state = self.start_num - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.state += self.step

        if self.state >= self.stop_num:
            raise StopIteration

        return self.state


my_range = MyRange(0, 10, 3)
# next(my_range) -> 0
# next(my_range) -> 1
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# try:
#     print(next(my_range))
# except StopIteration:
#     pass
for i in my_range:
    print(i)

print("FINSIHED")