import random

# Generate random number with random.randint
random_integer = random.randint(1, 10)
print(random_integer)

# Generating random number with random.random
random_float = random.random()
print(random_float)

# Create a random decimal number between 0 and 5.
random_decimal = random_float * 5
print(random_decimal)

# Example of use for random numbers.
love_score = random.randint(0, 100)
print(f"Yout love score is {love_score}.")
