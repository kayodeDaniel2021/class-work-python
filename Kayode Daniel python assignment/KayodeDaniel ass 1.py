# FOR DAY ONE ASSIGNMENT

# 1. Write a variable assign to a value, use the format method to print an output.
# 2. Get a variable name and use the arithmetic operators to add, minus, divide and multiply.
# 3. write a code to calculate the division of two numbers and round it up to the nearest whole number 
# """

# # Solution
# # Variable assignment and format method
# value = 35
# print(f"The assigned value is: {value}")

# # Arithmetic operations on variables
# variable1 = float(input("Enter the first number: "))
# variable2 = float(input("Enter the second number: "))

# addition_result = variable1 + variable2
# subtraction_result = variable1 - variable2
# division_result = variable1 // variable2
# multiplication_result = variable1 * variable2

# print("Addition Result: ", addition_result)
# print("Subtraction Result: ", subtraction_result)
# print("Division Result: ", division_result)
# print("Multiplication Result: ", multiplication_result)

# # Calculate division and round to the nearest whole number
# numerator = float(input("Enter the numerator: "))
# denominator = float(input("Enter the denominator: "))

# # we use the round function to round up.
# division_result_rounded = round(numerator / denominator)

# print("Division Result (Rounded):", division_result_rounded)


# Number 1: 
# Using examples, explain the difference between a Tuple and List

# LIST
# List are created using square bracket in listing items
# it can contain different data types: int, string, bool, etc

# Example:
# thislist = ["Kay", 1981, "May", "Jay@50", "Ray"]
# print(thislist)

# TUPLES
# Tuples uses the round brackets
# Tuples items CANNOT be deleted or added to
# Tuples items are unchangeable

# Example:
# desserts = ("icecream", "cakes", "cookies")
# print(desserts)
# print(type(desserts))
# print(len(desserts))
# print(desserts[-2])

# Number 2
# Using examples, explain string formatting

# String Formatting is used to make sure that a string is display the way it should
# Format() method is used to format a selected part of a string
# To control such value, place holders - curly brackets {} are used
# Example

# price = 150
# txt = "The price is {} naira"
# print(txt.format(price))

# For multiple values

# Qty = 35
# Itemno = 124
# Price = 60

# mytxt = "I need {} of item number {} at {:.2f} naira"
# print(mytxt.format(Qty, Itemno, Price))


# Number 3:
# Using x and y as variables perform calculations 
# using these operators (=, *, -, and /)

# x = 60
# y = 3

# a = x+y
# b = x*y
# c = x-y
# d = x//y     
  
# print(a)
# print(b)
# print(c)
# print(d)
