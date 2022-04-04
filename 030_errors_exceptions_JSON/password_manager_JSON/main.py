from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    letters_list = [password_list.append(choice(letters)) for letter in range(randint(8, 10))]
    symbols_list = [password_list.append(choice(symbols)) for symbol in range(randint(2, 4))]
    numbers_list = [password_list.append(choice(numbers)) for number in range(randint(2, 4))]

    shuffle(password_list)

    # Use .join to join items in a list, a tuple, or a dict.
    password = "".join(password_list)
    password_input.insert(0, string=password)
    # Use pyperclip to copy the password.
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Save passwords into a data.json file."""
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Hey!", message="It appears that you've left an empty field.")
    else:
        try:
            with open('data.json', 'r') as f:
                # Reading old data.
                data = json.load(f)  # Converts into a python dict.
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)  # Use indent to save json in a readable format.
        else:
            # Updating old data with new data.
            data.update(new_data)

            with open('data.json', 'w') as f:
                # Saving updated data.
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')
            website_input.focus()

# ---------------------------- FIND PASSWORD ---------------------------#


def find_password():
    """Check if the user's website is already stored and print it in another window."""
    website = website_input.get()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

# Create window.
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create canvas.
canvas = Canvas(width=200, height=200)

# Insert image into canvas.
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Create labels.
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create inputs.
website_input = Entry(width=33)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(index=0, string="felipesebben@yahoo.com.br")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Create buttons.
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

password_button = Button(text="Generate Password", width=14, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
