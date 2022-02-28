class Employee:
    minimum_salary = 18000

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = None
        self.salary = salary

    # Getter
    @property
    def salary(self):
        return self.__salary

    # Setter
    @salary.setter
    def salary(self, new_salary):
        print("IN setter")
        if new_salary < self.minimum_salary:
            pass
        else:
            self.__salary = new_salary

    def is_salary_above_thousand(self):
        return self.__salary >= 60000

toshe = Employee("Toshe", "Petrovski", int(input("What is your salary: ")))

# print(toshe.__salary)
print(toshe.salary)

new_salary = int(input("Please enter updated salary: "))
toshe.salary = new_salary

print(toshe.salary)