class Company:

    # special type of methods, dunder __init__
    # self is special attribute, which is a reference to the object being created
    def __init__(self, name, address, company_id):
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []

    def make_offer(self, employee, salary, position):
        if not isinstance(employee, Employee):
            raise Exception("employee parameter must be of class Employee")

        offer = Offer(self, employee, salary, position)
        offer.send_offer()

    def fire(self, employee):
        print(f"{self.name} is firing {employee.full_name()}")

        self.employee_list.remove(employee)

        employee.salary = None
        employee.position = None
        employee.company = None

    def get_salary_costs(self):
        # to return total salary cost of a company per month
        total_salary_costs = 0

        for employee in self.employee_list:
            total_salary_costs += employee.salary

        return total_salary_costs

    def __str__(self):
        # gives you text representation of instaces of the class
        return self.name


class Employee:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        self.salary = None
        self.position = None
        self.company = None

        self.offers = dict()

    def __str__(self):
        # gives you text representation of instaces of the class
        return self.full_name()

    def wake_up_for_work(self, time):
        print(f"Waking up for work, at: {time}")

    def check_expected_salary(self, salary):
        if salary < 25000:
            raise Exception(f"Salary offered {salary} is under expected salary of 25000")

        print("Expected salary is satisfied")

    def receive_offer(self, offer):
        if not isinstance(offer, Offer):
            raise Exception(f"{offer} is not an instance of class Offer. Can't process the request.")

        self.offers[offer.company.company_id] = offer

    def accept_offer(self, company):
        my_offer = self.offers.get(company.company_id)

        if not my_offer:
            raise Exception(f"No offer found from company {company}")

        self.salary = my_offer.salary
        self.position = my_offer.position
        self.company = my_offer.company
        self.company.employee_list.append(self)

        print(f"{self} has accepted the offer from {company}")

        del self.offers[company.company_id]

    def full_name(self):
        return self.first_name + " " + self.last_name

# Class Offer
# 1. we must define the attributes of the instances created  ///
# 2. we must create method, or call some method to send the offer to the potential employee  ///
# 3. validate the instance offer created

class Offer:
    minimum_salary = 18000

    def __init__(self, company, employee, salary, position):
        if salary < self.minimum_salary:
            raise Exception(f"Offer salary must be equal or above minimum salary of {self.minimum_salary}")

        self.company = company
        self.employee = employee
        self.salary = salary
        self.position = position

    def send_offer(self):
        self.employee.receive_offer(self)


class Developer(Employee):

    def __init__(self, first_name, last_name, email):
        # initialize the parent class
        # super() function return reference to non-initialied object of parent class
        super().__init__(first_name, last_name, email)
        # attribute overwritting
        self.position = "Software Developer"
        self.job_risk = "low"
        self.asset = "develop software solutions"

    def check_expected_salary(self, salary):
        if salary < 40000:
            raise Exception(f"Salary offered {salary} is under expected salary of 40000")

        print("Expected salary is satisfied")

class Accountant(Employee):

    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.position = "Accountant"
        self.job_risk = "low"
        self.asset = "calculate company financials"

    def wake_up_for_work(self, time):
        if time.startswith("09") or time.startswith("10") or time.startswith("11"):
            return super().wake_up_for_work(time)

        raise Exception("I only wake up between 09:00 and 11:00")


class PoliceOfficer(Employee):

    def __init__(self):
        self.position = "Police Officer"
        self.job_risk = "high"
        self.asset = "secure society"



# toshe = Developer("Toshe", "Petrovski", "toshe@gmail.com")
# print(toshe.salary)
toshe = Accountant("Toshe", "Petrovski", "toshe@gmail.com")
toshe.wake_up_for_work("12:30")

# toshe.check_expected_salary(30000)










semos = Company("Semos DOO", "Jane Sandanski", 1234)
seavus = Company("Seavus ADD", "Boris Trajkovski br. 4", 5678)

toshe = Employee("Toshe", "Petrovski", "toshe@gmail.com")
goran = Employee("Goran", "Markovski", "goran@gmail.com")
vesna = Employee("Vesna", "Markovska", "vesna@yahoo.com")

# semos.make_offer(goran, 50000, "Web Developer")
# goran.accept_offer(semos)
#
# semos.make_offer(vesna, 100000, "Python developer")
# vesna.accept_offer(semos)
#
# print(f"Semos total salary costs per month is: {semos.get_salary_costs()}")
# # print(semos.employee_list)

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

