# Debugging

# 1. Describe the problem.
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")


# my_function()


# 2. Reproduce the bug.
# from random import randint
# dice_imgs = ['1', '2', '3', '4', '5', '6']
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num - 1])

# 3. Play computer.
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You're a millenial.")
# elif year >= 1994:
#     print("You're a Gen Z.")

# 4. Fix the errors.
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# 5. Print is your friend.
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

# 6. Use a debugger.

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 4, 5, 8, 13])
