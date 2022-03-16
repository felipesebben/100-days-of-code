# for number in range(1, 101):
#     if number % 3 == 0 or number % 5 == 0:
#           'or' will accept any of the two conditionals as 'True'
#         print("FizzBuzz")
#      Two sequential if statements followed by and else, which will only
#      consider the last if statement, printing any number that is not
#      divisible by 5.
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         [] will print a list
#         print([number])


# Answer.
for number in range(1, 101):
    # print(f"Currently on number {number}") to check what's being printed
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
