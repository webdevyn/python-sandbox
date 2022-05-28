# prints 0 through 10
# for value in range(11):
#     print(f"{value} is the number")

# starts with 2, adds 2 until 11 is reached/passed
# even_nums=list(range(2,11,2)) 
# print(even_nums)

# list of squares of nums 1-10
# squares=[]
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)

# list of squares using list comprehension
squares=[value**2 for value in range(1,11)]
print(squares)