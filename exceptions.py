# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
# embg = input("Please enter your embg: ")
#
# if not embg.isdigit():
#     raise Exception("Your EMBG must contain only digits")
# elif len(embg) != 13:
#     raise Exception("Your EMBG must contain exactly 13 digits.")
#
# print("Finished")


def send_sms(phone_number, msg):
    if len(phone_number) < 7 or len(phone_number) > 13:
        raise Exception("Invalid phone number")

    print(f"Sending sms with text: {msg}, to phone number: {phone_number}")



# first_name = input("Please enter first name: ")
# phone_number = input("Please enter your phone number: ")
#
# message = f"Hi {first_name}, welcome to our website."
#
# counter = 1
#
# while counter <= 3:
#     try:
#         send_sms(phone_number, message)
#         break
#     except:
#         counter += 1
#         print(f"You phone number: {phone_number}, is invalid. Please enter valid number.")
#         phone_number = input("Please enter your phone number: ")
#
#
# if counter == 3:
#     print("Stopping program, 3 times entered invalid phone number.")
# else:
#     print("Thank you for registering to our website.")
#

try:
    with open("test_file.txt", "r") as f:
        f.read()
except FileNotFoundError as exc:
    print(exc)
except IndexError:
    print("IN index error")
else:
    print("File was opened succeessfully")

