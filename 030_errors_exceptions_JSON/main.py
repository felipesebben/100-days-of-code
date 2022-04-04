# FileNotFound
# with open("a_file.txt") as f:
#     f.read()


# KeyError - tapping into a key that does not exist.
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError - getting an item from non-existent index
# fruit_list = ["Apple", "Banana", "Pineapple"]
# fruit = fruit_list[3]

# TypeError - trying to something with a data, and it was designed for that.
# text = "abc"
# print(text + 5)


# ------ HANDLING EXCEPTIONS ------- #

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    # print("There was an error.") - too broad and does not fix our problem - you have to fix it!
    file = open("a_file.txt", "a")
    file.write("Something")
except KeyError as error_message:  # Get hold of error message
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("There is an error that I made up.")
    file.close()
    print("File was closed.")


# Raise errors - why raising them in first place?

height = float(input("Height: "))
weight = int(input("Weight: "))

# Raise your own exception to avoid absurd inputs.
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)