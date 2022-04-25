# ---------- TYPE HINTS ----------- #

# Make your code less error-prone by setting a type to a variable.
# age: float
# name: str
# height: float
# is_human: bool

# Specify the data type in the function. Specify the output of the function with "->".
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


# String will be highlighted, as int was expected.
if police_check("twelve"):
    print("You may pass.")
else:
    print("Pay a fine.")

# Will call a type error
# age = "twelve"
# name = 12

