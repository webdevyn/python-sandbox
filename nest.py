# # make an empty list for storing aliens
# aliens = []

# # make 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color':'green', 'points':5, 'speed':'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# # show the first 5 aliens
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # show how many aliens have been created
# print(f"Total num of aliens: {len(aliens)}")

# # pizza info
# pizza = {
#     'crust':'thick',
#     'toppings':['mushrooms','no cheese'],
# }
# # summarize order
# print(f"You ordered a {pizza['crust']}-crust pizza "
# "with the following toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")

users = {
    'aeinstein': {
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },

    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}
# username is key and user_info is value
for username, user_info in users.items():
    print(f"\nUsername: {username}")

    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
