# person = {
#     "first_name": "Sherlock",
#     "last_name": "Holmes",
#     "age": 40,
#     "city": "London"
# }

# print(f"The person dictionary contains: {person}")
# print(f"Name is {person['first_name']} {person['last_name']} ")
# print(f"Age is {person['age']}")
# print(f"City is {person['city']}")

# favNums = {
#     "Sally": 5,
#     "Juliet": 3,
#     "Roger": 24,
#     "James": 15,
#     "Dalton": 13
# }

# print(f"Sally's fav num is: {favNums['Sally']}")
# print(f"Juliet's fav num is: {favNums['Juliet']}")
# print(f"Roger's fav num is: {favNums['Roger']}")
# print(f"James's fav num is: {favNums['James']}")
# print(f"Dalton's fav num is: {favNums['Dalton']}")

# loop through each item in dictionary
# can use any vars for words key,value

# favNums.update( [("Jerry", 76),("Bernice",9)])
# print(favNums)

# for key,value in favNums.items():
#     print(f"\nName: {key}")
#     print(f"Favorite Number: {value}")


# for num in favNums.:
#     print(num.title())

# friends = ['Carrie', 'James']
# for name in favNums.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         num = favNums[name]
#         print(f"\t{name.title()}, I see you love {num}!")

# if 'erin' not in favNums.keys():
#     print("Erin, please tell us your favorite number!")

# for name in sorted(favNums.keys()):
#     print(f"{name.title()}, thanks for sharing.")

# print("The following numbers are favorites:")
# for num in favNums.values():
#     print(num)

# rivers = {
#     "nile": "egypt",
#     "amazon": "brazil",
#     "mississippi": "united states"
# }

# for k,v in rivers.items():
#     print(f"The {k.title()} runs through {v.title()}.")

names = ["janice", "judy", "bart", "sally", "roger", "james"]
favNums = {
    "sally": 5,
    "juliet": 3,
    "roger": 24,
    "james": 15,
    "dalton": 13
}

for name in favNums.keys():
    print(f"Hi {name.title()}, thanks for sharing.")

for name in names:
    if name not in favNums.keys():
        print(f"Hi {name.title()}, please tell us your favorite number!")
