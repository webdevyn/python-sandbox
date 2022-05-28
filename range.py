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
# squares=[value**2 for value in range(1,11)]
# print(squares)

# exercises
# for value in range(1, 21):
#     print(value)

# nums=[value for value in range(1, 1000001)]
# print(nums)
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# odd_nums=[num for num in range(1,21)]
# for num in odd_nums:
#     if num%2 != 0:
#         print(num)

# odd_nums=[num for num in range(1,21,2)]
# print(odd_nums)

# threes=[num for num in range(3,31,3)]
# print(threes)

cubes=[num**3 for num in range(1,11)]
print(cubes)