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