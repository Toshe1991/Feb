







class Company:

    # special type of methods, dunder __init__
    # self is special attribute, which is a reference to the object being created
    def __init__(self, name, address, company_id):
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []

    def hire(self, employee, position, salary):
        if salary < Employee.minimum_salary:
            raise Exception(f"Salary must be equal or over {Employee.minimum_salary}")

        print(f"{self.name} is hiring {employee.full_name()}")

        employee.position = position
        employee.salary = salary
        employee.company = self

        self.employee_list.append(employee)

    def fire(self, employee):
        print(f"{self.name} is firing {employee.full_name()}")

        self.employee_list.remove(employee)

        employee.salary = None
        employee.position = None
        employee.company = None

    # get_salary_costs method
    # to return total salary cost of a company per month

    def __str__(self):
        # gives you text representation of instaces of the class
        return self.name


class Employee:
    minimum_salary = 18000

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        self.salary = None
        self.position = None
        self.company = None

    def __str__(self):
        # gives you text representation of instaces of the class
        return self.full_name()

    def full_name(self):
        return self.first_name + " " + self.last_name


semos = Company("Semos DOO", "Jane Sandanski", 1234)
seavus = Company("Seavus ADD", "Boris Trajkovski br. 4", 5678)

toshe = Employee("Toshe", "Petrovski", "toshe@gmail.com")
goran = Employee("Goran", "Markovski", "goran@gmail.com")
vesna = Employee("Vesna", "Markovska", "vesna@yahoo.com")

# semos.hire(vesna, "Senior Software Developer", 17000)

# isinstance(object, class) -> if object is instance of class
print(isinstance(semos, Employee))

# print(f"Name: {vesna.full_name()}, Postion: {vesna.position}, Company: {vesna.company}")
#
# print("Employees in Semos DOO: ")
# for employee in semos.employee_list:
#     print(employee)
#
# semos.fire(vesna)
# print(f"Name: {vesna.full_name()}, Postion: {vesna.position}, Company: {vesna.company}")
#
# print("Employees in Semos DOO: ")
# for employee in semos.employee_list:
#     print(employee)

# vesna.salary = 50000
# vesna.position = "HR"
# vesna.company = semos

# print(f"Vesna works at company: {vesna.company}, with address: {vesna.company.address}")
# print(toshe.full_name())
# print(goran.full_name())
# print(vesna.full_name())

# __dict__ -> returns all attributes with key:value pairs as dictionary
# return -> self.__dict__["email"]
# print(toshe.__dict__["email"])

# dir(arg) -> description of all dunder attributes and methods for a class
# print(dir(toshe))

# syntactic sugar
# toshe.email
# Python all attributes keeps them in dictionary
# print(toshe.email)












# class Host:
#
#     def __init__(self, ip, domain, name, exists):
#         self.ip = ip
#         self.domain = domain
#         self.name = name
#         self.exists = exists
#
#
# live_servers = []
# base_ip = "192.168.1.{}"
#
# for i in range(25, 50):
#     ip = base_ip.format(i)
#     # ping to ip
#     is_alive = True
#     if is_alive:
#         host = Host(ip, "abv", f"Server: {ip}", exists=True)
#         live_servers.append(host)
#
#
# for host in live_servers:
#     print(host.name)
#











# name = input("Please enter your company name: ")
# address = input("Please enter your company address:")

# company = Company(input("Please enter your company name: "), input("Please enter your company address:"))
# print(f"Company name: {company.name}, Company address: {company.address}")
# # self is implicitly passed by Python
# semos = Company("Semos DOO", "Jane Sandanski")
# seavus = Company("Seavus ADD", "Boris Trajkovski br. 4")
#
# print(f"Company name: {semos.name}, Company address: {semos.address}")
# print(f"Company name: {seavus.name}, Company address: {seavus.address}")

# semos.name = "Semos DOO"
# semos.address = "Jane Sandaski"
#
# print(semos.company_id)

# creating instance from a class
# every instance defined from our own class is mutable
# semos = Company()
#
# # dot syntax, if we want to define object attributes we use object.attribute
# semos.name = "Semos DOO"
# semos.address = "Jane Sandaski"

# company = semos
#
# company.name = "Unknown"
# print(semos.name)
# print(company.name)
# # print(id(semos))
# # print(id(company))
#
#
#
#
# seavus = Company()
# seavus.name = "Seavus ADD"
# seavus.address = "Boris Trajkovski br. 4"
#
# # print(id(semos))
# # print(id(seavus))

# print(type(semos))
# print(type("Hello"))
# print(f"Company name: {semos.name}, Company address: {semos.address}")

