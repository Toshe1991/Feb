# # f = open("test_file.txt", "w")
# #
# # f.write("Hello from python course\n")
# # f.write("This is my second line\n")
# # f.write("This is my third line\n")
# #
# # f.close()
#
# # f = open("test_file.txt", "r")
#
# # content = f.read(10)
# # content_list = f.readlines()
# # print(content_list)
# # f.close()
#
# # f = open("test_file.txt", "w")
# #
# # f.write("This is my fourth line")
# #
# # f.close()
#
# with open("test_file.txt", "a") as f:
#     f.write("Hello from seconds line\n")
#     f.write("Hello from third line\n")
#
# f.write("Hello from fourth line")


### CSV FILES ###

# first_name, last_name, phone_number
# Toshe     , Petrovski, 12345
# Bojan     , Kostadinov, 012345

# import csv
#
# with open("emails.csv", "r") as csv_file:
#     # csv_reader = csv.reader(csv_file, delimiter=";")
#     csv_reader = csv.DictReader(csv_file, delimiter=";")
#
#     for row in csv_reader:
#         print(row)
#
import csv

with open("employees.csv", "w") as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=",")

    employee_writer.writerow(["first_name", "last_name", "position"])
    employee_writer.writerow(["Toshe", "Petrovski", "HR"])
    employee_writer.writerow(["Darko", "Gjorgievski", "Developer"])









