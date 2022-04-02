from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_input = Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# TODO 4. Create buttons.
# Create buttons.
password_button = Button(text="Generate Password",width=14)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()