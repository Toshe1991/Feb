class Car:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.is_serviced = False

    def make_service(self):
        print(f"Servicing vehicle {self.brand}-{self.model}")
        self.is_serviced = True

    @staticmethod
    def calculate_distance(city):
        total_distance = {"Ohrid": 300, "Tetovo": 100}

        if city in total_distance:
            return total_distance[city]
        else:
            return -1

my_toyota = Car("Toyota", "Corolla", "white")

# make_service makes mutation of the instance attribute - it must be instance method
my_toyota.make_service()

print(Car.calculate_distance("Ohrid"))