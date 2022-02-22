# l = [10, 20, 30, 40]

# for number in l:
#     print(number ** 2)

# index = 0
#
# while index < len(l):
#     print(l[index] ** 2)
#     index += 1
#
# print("Finished")

fruits = ["apples", "oranges", "strawberries", "cherries"]
bucket = []

while True:
    item = input("Please enter product to add to bucket, or q/Q to quit: ")

    if item.lower() == "q":
        break
    elif item not in fruits:
        print(f"{item} is not available, please select one of: {fruits}")
        continue

    bucket.append(item)

    print("Current items in bucket:")
    for product in bucket:
        print(product)


print("Please proceed to checkout!!!")

















