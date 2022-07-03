class Car:
    """Simple representation of a car"""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Error - can't roll back odometer.")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Battery:
    """Model electric car battery"""

    def __init__(self,battery_size=75):
        """Initialize battery attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print stmt describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print stmt about battery range"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represent aspects of electric car"""

    def __init__(self,make,model,year):
        """Initialize attributes of the parent class"""
        super().__init__(make,model,year)
        """Initialize electric car attributes"""
        self.battery = Battery()

    def fill_gas_tank(self):
        """does not apply to electric cars"""
        print("This car doesn't need gas.")

my_500e = ElectricCar('fiat','model 500e',2019)
print(my_500e.get_descriptive_name())
print(f"{my_500e.odometer_reading} current miles.")
my_500e.increment_odometer(5000)
print(f"New mileage is: {my_500e.odometer_reading}")
my_500e.battery.describe_battery()
my_500e.battery.get_range()
my_500e.battery.upgrade_battery()
my_500e.battery.describe_battery()
my_500e.battery.get_range()
my_500e.fill_gas_tank()

class Restaurant:
    """a simple model of a restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        """initialize attributes"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe(self):
        """print info about restaurant"""
        print(f"{self.name} serves {self.type} food.")

    def open(self):
        """prints restaurant is open"""
        print(f"{self.name} is open!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, incrm):
        self.number_served += incrm


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors=["vanilla","chocolate","caramel"]):
        """Initialize attributes of the parent class"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"{self.flavors} are the flavors we have.")


my_Stand = IceCreamStand('Coldies','Nondairy')
print(f"{my_Stand.name} serves {my_Stand.type} frozen treats.")
my_Stand.display_flavors()
