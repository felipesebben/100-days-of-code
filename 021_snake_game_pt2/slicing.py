# Slicing

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# Print 'c', 'd', and 'e'
print(piano_keys[2:5])

# Slice from pos 2 till the end.
print(piano_keys[2:])

# Slice everything up to pos 5.
print(piano_keys[:5])

# Slice from pos 2 till 5 with intervals.
print(piano_keys[2:5:2])

# Get every second item.
print(piano_keys[::2])

# Specify -1 to reverse list, printing it from the end till beginning.
print(piano_keys[::-1])

# Slicing works with tuples too.
print(piano_tuple[1:])