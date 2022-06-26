# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print(f"\nThese models have been printed: ")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

def build_sandwich(*toppings):
    print(f"\n The sandwich will contain: ")
    for topping in toppings:
        print(f"-{topping}")

build_sandwich('tomatoes', 'mushrooms', 'onions', 'olives')
