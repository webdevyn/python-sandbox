# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())    #removes the \n
  
# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())
# print(lines)

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    print(f"lines: {lines}")
    print(f"orig pi_string: {len(pi_string)} chars")
    pi_string += line.strip()
    print(pi_string)
    print(f"length of string: {len(pi_string)}")