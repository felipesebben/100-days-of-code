# Class inheritance.

# It means inheriting methods already defined in another class.
# This process is also applicable to attributes, as well as behavior.

# Example:
# class Fish(Animal): # Fish class will inherit from Animal class.
#     def __init__(self)
#         super().__init__()  # Add super(), which refers to the super class - everything the super class can do


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):  # Allows the class to inherit all attributes and methods from the super class (Animal).
    def __init__(self):
        super().__init__()  # The call to super() initializer is recommended yet not mandatory.

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
