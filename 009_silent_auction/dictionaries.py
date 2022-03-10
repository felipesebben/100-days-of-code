programming_dictionary = {
    "Bug": "An error in a program that prevents the program" +
    "from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from dictionary.
# print(programming_dictionary['Bug'])

# Add new entry to a dictionary.
programming_dictionary['Loop'] = ("The action of doing something over and, "
                                  "over again.")

# Create an empty dictionary.
empty_dictionary = {}

# Wipe and existing dictionary. Clears out previous dicts.
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary.
programming_dictionary['Bug'] = """A moth in your computer."""
print(programming_dictionary["Bug"])


# Loop through a dictionary returning keys.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
