# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by zero")

# print("enter 2 numbers to be divided")
# print("enter q to quit")

# while True:
#     first_num = input("\nFirst Number: ")
#     if first_num == "q":
#         break
#     second_num = input("\nSecond Number: ")
#     if second_num == "q":
#         break
#     try:
#         answer = int(first_num)/int(second_num)
#     except ZeroDivisionError:
#         print("no dividing by zero!")
#     else:
#         print(answer)

filename = 'alice.txt'

try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")