# Simple function.
def greet():
    '''
    Print three simple statements.
    '''
    print("Hello, coder!")
    print("\nThis is a simple function in which the should read...")
    print("\n...three statements!")

# greet()

# Function that allows for input.


def greet_with_name(name):
    '''
    Greet person with his or her name.
    '''
    print(f"Hello, {name}!")
    print(f"How are you, {name}?")

# greet_with_name("Felipe")

# Functions with more than 1 input.


def greet_with(name, location):
    '''
    Greet person with name and location.
    '''
    print(f"Hello, {name.title()}!")
    print(f"How's the weather in {location.title()}?")


# greet_with("livia", "anta gorda")

# Functions with keyword arguments.
greet_with(location="anta gorda", name='livinha')
