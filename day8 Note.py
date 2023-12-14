'''
- Object Oriented Programming(OOP)
- Classes in Python
- Creating Classes
- Instance Methods
'''

''' 
Object-Oriented Programming (OOP) is a programming paradigm that is based on the concept of objects. 
These objects are instances of classes, which are user-defined blueprints or templates for creating objects. 
OOP is a way of organizing and designing code to model real-world entities and their interactions more naturally.
Classes allow you to encapsulate related data and functions into a single entity, making your
code more organized and reusable
'''

'''OOP'''
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)


# timmy.right(90)

# def square():
#     for move in range(4):
#         timmy.forward(100)
#         timmy.right(90)
    
# square()
# my_screen = Screen()
# print(my_screen.canvheight, my_screen.canvwidth)
# my_screen.exitonclick()

'''CREATING CLASSES'''
# class User:
#     pass

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Phace"

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Joy"
# print(user_1.username, user_2.username)

'''BETTER WAY OF WRITING CLASSES'''
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
  


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
# 
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

'''OTHER EXAMPLES'''
# '''001 - Simple Class Definition and Object Creation: '''
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

# my_car = Car("Toyota", "Camry")
# print(f"My car is a {my_car.make} {my_car.model}")


'''002 - Attributes and Methods'''
# class Circle:
#     pi = 3.14159265359

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return self.pi * self.radius ** 2

# my_circle = Circle(5)
# print(f"Circle area: {my_circle.area()}")


'''003 - Encapsulation and Getter/Setter Methods'''
# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance

#     def get_balance(self):
#         return self._balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#         else:
#             print("Insufficient funds")

# my_account = BankAccount(1000)
# my_account.withdraw(500)
# my_account.deposit(5000)
# print(f"Remaining balance: {my_account.get_balance()}")