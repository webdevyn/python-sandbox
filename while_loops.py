# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# # verify each user until there are no more unconfirmed users
# # move each verified user into list of confirmed users

# while unconfirmed_users:      # only runs while list is not empty
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)


# # display all confirmed users

# print("\nThe followig users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# responses = {}

# polling_active = True

# while polling_active:
#     # Prompt for the person's name and response.
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
    
#     # Store the response in the dictionary:
#     responses[name] = response
    
#     # Find out if anyone else is going to take the poll.
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
        
# # Polling is complete. Show the results.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")



# sandwich_orders = ['deluxe', 'mushroom', 'italian']
# finished_sandwiches = []

# for sandwich in sandwich_orders:
#     print(f"I made your {sandwich} sandwich.")
#     finished_sandwiches.append(sandwich)
# print("These sandwiches have been made: ")
# for sandwich in finished_sandwiches:
#     print(sandwich)

# sandwich_orders = ['pastrami','deluxe','pastrami', 'mushroom','pastrami', 'italian']
# finished_sandwiches = []

# print(f"We have run out of pastrami!")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# for sandwich in sandwich_orders:
#     print(f"I made your {sandwich} sandwich.")
#     finished_sandwiches.append(sandwich)
# print("These sandwiches have been made: ")
# for sandwich in finished_sandwiches:
#     print(sandwich)



responses = {}
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Where would you like to go? ")
    
    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to go to " + response + ".")