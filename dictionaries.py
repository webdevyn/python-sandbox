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

favNums = {
    "Sally": 5,
    "Juliet": 3,
    "Roger": 24,
    "James": 15,
    "Dalton": 13
}

print(f"Sally's fav num is: {favNums['Sally']}")
print(f"Juliet's fav num is: {favNums['Juliet']}")
print(f"Roger's fav num is: {favNums['Roger']}")
print(f"James's fav num is: {favNums['James']}")
print(f"Dalton's fav num is: {favNums['Dalton']}")

# loop through each item in dictionary
# can use any vars for words key,value
for key,value in favNums.items():
    print(f"\nName: {key}")
    print(f"Favorite Number: {value}")