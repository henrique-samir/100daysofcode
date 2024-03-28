# adding = 4 + 3
# print(adding)

# subtraction = 8 - 9
# print(subtraction)

# multiplication = 4 * 32
# print(multiplication)

# division = 50 / 5
# print(division)

# squared = 5**2
# print(squared)

# # resto
# modulo = 15 % 4
# print(modulo)

# # inteiro
# divisor = 15 // 2
# print(divisor)

# Solve the following problems with my code
# Your goal is to print the solution of all 3 calculations to the screen.

# multiplication
# mult = 3.4 * 6.8
# print(mult)

# # division
# div = 2467 / 4673
# print(div)

# #raise 10 to the power of 2
# square = 10 ** 2
# print(square)

# # print the remainder when 343 is divided by 4
# module = 343 % 4
# print(module)

my_bill = float(input("What was the bill?: "))
number_of_people = int(input("How many people?: "))
tip = int(input("What percentage do you want to tip?: "))
answer = (tip / 100 * my_bill + my_bill) / number_of_people
print("You all owe", round(answer, 2))
