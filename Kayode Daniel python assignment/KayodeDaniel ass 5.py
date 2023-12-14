# FOR DAY FIVE ASSIGNMENT
# Write a simple program for a simple calculator or atm machine 
# based on all the knowledge of what you have learnt so far,
# which must include use of the def function, if/else/elif statement 

# To write a simple program for a simple calculator.
    
# USING A DEF FUNCTION.

# In python, a function is defined using def keyword.
# A function is a block of code which runs when it is called.
# To call a function, use the function name followed by parenthesis():
# A function can return data as a result
# is the most used keyword in python

# to add two numbers
def add(num1, num2):
    return num1 + num2
print("1. add\n")                          # is a type of escape character ti indicate end of a line

# to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
print("2. subtract\n")

# to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
print("3. multiply\n")

# to divide two numbers
def divide(num1, num2):
    return num1 // num2
print("4. divide\n")

# USING IF/ELSE/ELIF STATEMENT
# take input from the User
select = int(input("select operations from 1, 2, 3, 4:"))

number_1 = int(input("enter first number: "))
number_2 = int(input("enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))

else:
    print("invalid input")