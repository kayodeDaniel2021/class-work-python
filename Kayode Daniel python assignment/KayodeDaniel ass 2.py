# FOR DAY TWO ASSIGNMENT

# Question 1. 
# Create a grocery list containing at least 6 items.
 
# Grocery = ["Garri", "Wheatflour", "Plantainflour", "Indomie", "PalmOil", "KnorCube"]
# print(Grocery)

# 2. Write a python program to print the indexes 
# of the previously created list using the following index 
# (index 2, 2 till end, 4 and 5)

# Grocery = ["Garri", "Wheatflour", "Plantainflour", "Indomie", "PalmOil", "KnorCube"]
# print(Grocery[2])
# print(Grocery[2:])
# print(Grocery[4:5])


# Question 3
# Write a program to append, insert, extend, remove to the list

# to append means to add to the list
# using append() method to append a list

# Grocery = ["Garri", "Wheatflour", "Plantainflour", "Indomie", "PalmOil", "KnorCube"]
# Grocery.append("DryFish")
# print(Grocery)

# to insert, it does at a specified Index
# to insert an item as the second position

# Grocery.insert(2, "Egusi")
# print(Grocery)


# MoreGrocery = ["TissuePaper", "Ziplock", "Toothpick"]
# Grocery.extend(MoreGrocery)
# print(Grocery)

# Grocery.remove("Garri")
# print(Grocery)
# Grocery.remove(Grocery[1])
# print(Grocery)


# Question 4 
# Create a NESTED DICTIONARY using different 3 kinds of phones 
# and their keys should be name, model, storage and ram. 
# use the update method to change the ram size of the second phone.

# PHONES' DICTIONARY

# phone = {
#     "phone1" : {
#         "name" : "iphone" ,
#         "model" : "iphone11promax" ,
#         "storage" : 256 ,
#         "ram" : "8G"
#     },
#     "phone2" : {
#         "name" : "samsung" ,
#         "model" : "A50" ,
#         "storage" : 128 ,
#         "ram" : "8G"
#     },
#     "phone3" : {
#         "name" : "nokia" ,
#         "model" : 3310 ,
#         "storage" : 64 ,
#         "ram" : "4G"
#     },

#  }

# print(phone)
# phone["phone2"].update({"Ram": "12 G"})
# print(phone)
