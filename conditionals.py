# cars = ["audi", "bmw", "toyota", "lexus"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# print("audi" in cars)

# banned_users = ["andrew", "caroline", "david"]
# user = "jane"

# if user not in banned_users:
#     print(f"{user.title()}, you are allowed to post.")

# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40

# print(f"Your admission cost is ${price}")

# alien_color = "green"

# if alien_color == "green":
#     print(f"Player earns 5 points")
# else:
#     print("No points awarded")

# avail_toppings = ['mushrooms', 'olives', 'green peppers', 'pineapple', 'basil', 'tomatoes']
# request_toppings = ['mushrooms', 'artichokes', 'garlic']

# for request_topping in request_toppings:
#     if request_topping in avail_toppings:
#         print(f"Adding {request_topping}")
#     else:
#         print(f"Sorry, we don't have {request_topping}")

# print("\nFinished making your pizza")

# users = ('admin', 'sally', 'tom', 'jackie', 'rosie')

# if users:
#     for user in users:
#         if user == 'admin':
#             print(f"Hello {user}, would you like a status report?")
#         else:
#             print(f"Hello {user}, welcome back.")
# else: 
#     print('There are no users.')

# current_users = ['admin', 'sally', 'tom', 'june', 'rosie']
# new_users = ['june', 'jerry', 'rosie', 'lucy', 'dale']

# for new_user in new_users:
#     if new_user in current_users:
#         print(f"Sorry, {new_user.title()}, that user name is taken. Please choose another user name.")
#     else:
#         print(f"Hello {new_user.title()}, welcome to the site!")

ord_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in ord_nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num ==3:
        print("3rd")
    else:
        print(f"{num}th")