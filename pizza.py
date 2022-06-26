def make_pizza(size, *toppings):
    """summarize the pizza that will be made"""
    print(f"\nMaking a {size}-inch pizza with these toppings: ")
    for topping in toppings:
        print(f"-{topping}")