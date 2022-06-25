
# def display_message():
#     """Displays message about learning functions."""
#     print("This chapter covers functions.")

# display_message()

# def fav_book(book_input):
#     """Displays favorite book"""
#     print(f"{book_input.title()} is my favorite book.")

# fav_book("sherlock holmes")

# def make_shirt(size="L", text="I love Python"):
#     print(f"Shirt size is {size} and says {text}.")

# make_shirt("M", "smile it's Friday")
# make_shirt()


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nEnter your name:")
#     print("\n(enter 'q' to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")
    


def city_country(city, country):
    """Return a city and country"""
    city_country_full = f"{city}, {country}"
    return city_country_full.title()

while True:
    print("Enter a city: ")
    print("(q to quit)")

    city_name = input("City: ")
    if city_name == 'q':
        break

    country_name = input("Country: ")
    if country_name == 'q':
        break

    formatted = city_country(city_name, country_name)
    print(f"{formatted} is a great place!\n")
