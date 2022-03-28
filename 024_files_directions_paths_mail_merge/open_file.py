# Open a file by storing it in a variable with the open() method.
# with open("my_file.txt") as f:
#     # The with clause will manage the file directly. As soon as we're done with it, it will close the file.
#     # Read it with .read().
#     contents = f.read()
#     print(contents)


# Writing a file - will delete what you'd had written before!
# with open("my_file.txt", mode='w') as f:
#     f.write("New text. ")

# To add new content, use mode='a' ("a" stands for "append")
# with open("my_file.txt", mode='a') as f:
#     f.write("\nNew text.")

# If you try to open a file which doesn't exist, the open() method will create it.
# Only works in "write" mode.

# with open("new_file.txt", mode='w')  as f:
#     f.write("New text. ")

# Opening a file with absolute path:
with open("/../../../../OneDrive/OneDrive/Área de Trabalho/my_file.txt", mode='r') as f:
    # The with clause will manage the file directly. As soon as we're done with it, it will close the file.
    # Read it with .read().
    contents = f.read()
    print(contents)
