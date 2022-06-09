# parrot
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\n  Enter 'quit' to end the program."
# message = ""

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)



prompt = "\nPlease enter a city you have visited."
prompt += "\n(Enter'quit' when you are finished.)\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
