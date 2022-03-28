PLACEHOLDER = "[name]"

with open('Input/Names/invited_names.txt', mode='r') as f:
    list_names = f.readlines()
    print(list_names)

with open('Input/Letters/starting_letter.txt', mode='r') as f:
    letter_contents = f.read()
    for name in list_names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as f:
            f.write(new_letter)
