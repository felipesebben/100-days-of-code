# Create a class to model our website users.
class User:  # Declaration - class should be Pascal Case (first letter capitalized, ie. UserName)

    def __init__(self, user_id, username):
        # It's going to be called every time you create a new object from this class (User).
        # Everytime there's a new object created, you must provide two arguments to the parameters (user_id, username).
        self.id = user_id
        self.username = username.title()
        self.followers = 0  # Set to a default value.
        self.following = 0
    # pass  # Use it if you want to leave function or class empty.

    # Create a method (DO SOMETHING).
    def follow(self, user): # A method ALWAYS needs a 'self' parameter; this way, it knows the object that called it.
        user.followers += 1
        self.following += 1


user_1 = User('001', 'felipe')  # Object
user_2 = User('002', 'jake')
# Working with attributes. An attribute is a variable which is associated with a variable. It is attached to an object.
# user_1.id = "001"
# user_1.username = "felipe"
# Attribute exists with the object.
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# If you want to create attributes to different variables, you need to deal with constructors.
# This is related to the concept of 'initialize', that is, to set variables to their starting values at the beginning
# of a program or subprogram.

# In python, the way that we would build the constructor is by using the __init__ function.
# class Car:

# -- Adding Methods to Class.
# Methods are things the object DOES.