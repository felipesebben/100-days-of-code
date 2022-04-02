from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    letters_list = [password_list.append(choice(letters)) for letter in range(randint(8, 10))]
    symbols_list = [password_list.append(choice(symbols)) for symbol  in range(randint(2, 4))]
    numbers_list = [password_list.append(choice(numbers)) for number in range(randint(2, 4))]

    shuffle(password_list)

    # Use .join to join items in a list, a tuple, or a dict.
    password = "".join(password_list)
    password_input.insert(0, string=password)
    # Use pyperclip to copy the password.
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
   """Save passwords into a data.txt file."""
   website = website_input.get()
   email = email_input.get()
   password = password_input.get()

   if len(website) == 0:
       messagebox.showinfo(title="Hey!", message="It appears that you've left the website field empty.")
   elif len(password) == 0:
       messagebox.showinfo(title="Hey!", message="It appears that you've left the password field empty.")
   else:
       is_ok = messagebox.askokcancel(title=website,
                              message=f"These are the details entered:"+
                                      f"\nEmail: {email} \nPassword: {password} \nIs it ok to save?")
       if is_ok:
          with open('data.txt', 'a') as f:
              f.write(f"{website} | {email} | {password}\n")
              website_input.delete(0, 'end')
              password_input.delete(0, 'end')
              website_input.focus()

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
# TODO 1. Set image layout.
canvas.grid(column=1, row=0)

# TODO 2. Create labels.
# Create labels.
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# TODO 3. Create entries.
# Create inputs.
website_input = Entry(width=51)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(index=0, string="felipesebben@yahoo.com.br")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# TODO 4. Create buttons.
# Create buttons.
password_button = Button(text="Generate Password",width=14, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()