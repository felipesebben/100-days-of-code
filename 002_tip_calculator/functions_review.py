# len(1334)  # Will get an error

num_char = len(input("What is your name?"))

# TypeError - can only concatenate str (not 'int') - cannot add str to int!

# Convert integer variable to string so you can concatenate between strings.
new_num_char = str(num_char)

# Type check function to make sure you know the dtype.
print(type(num_char))

print("Your name has " + new_num_char + " characters.")

# Change dtypes in many ways.
a = float(123)
print(type(a))

print(70 + float("100.5"))

print(int(8/3))

# Round function.
print(round(8/3))

# Specify number of digits.
print(round(8 / 3, 2))

# Use // to automatically convert to int.
print(type(8 // 3))

# Remember that divisions result in float.

# Continue calculations with variables.
result = 4 / 2
result /= 2
print(result)
# Result divided by two then divided by two once more.

# User scores a point.
score = 0
score += 1
height = 1.8
isWining = True
print(score)

# F strings - mix strings and different data types.
print(f"Your score is {score}, your height's {height}, your win's {isWining}.")
