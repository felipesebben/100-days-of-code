'''
You are going to write a program which will
select a random name from a list of names.
The person selected will have to pay for everybody's food bill.
'''
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


# Get the total number of items in the list.
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay.title()} is going to buy the meal today.")
