# class Dog:
#     """a simple model of a dog"""
#     def __init__(self,name,age):
#         """initialize name and age attributes"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)
# your_dog = Dog("Lucy", 3)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()

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

restaurant = Restaurant('Test Cafe', 'Italian')
print(f"{restaurant.name} serves {restaurant.type} food and has served {restaurant.number_served} people.")

restaurant.set_number_served(100)

print(f"\n{restaurant.name} has now served {restaurant.number_served} people.")

restaurant.increment_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)

# cafe1 = Restaurant('Apples and Barley', 'American')
# cafe2 = Restaurant('Crunchy Cafe', 'Healthy')

# print(f"The first cafe's name is {cafe1.name}.")
# print(f"{cafe1.name} serves {cafe1.type} food.\n")

# cafe1.describe()
# cafe1.open()
# cafe2.describe()
# cafe2.open()



