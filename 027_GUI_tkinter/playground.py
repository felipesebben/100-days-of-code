# Unlimited Positional Arguments.
# You can put an undetermined number of arguments to the function.


def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(2, 100, 200, 982))


# **kwargs : Many Keyword Arguments
#  You can call this function, pass in a keyword argument, such as add, and turn them into **kwargs,
#  which are basically dicts.

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5) # Each keyword argument becomes a key, and their value, a value.


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')  # Get will return None if no value is given, avoiding errors.
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')


my_car = Car(make='Nissan', model='GT-R')
print(my_car.model)