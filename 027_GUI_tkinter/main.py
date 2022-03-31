from tkinter import *


def button_clicked():
    print("I Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Create components

# Label
my_label = Label(text="I Am a Label", font=('Helvetica', 24, 'bold'))
# my_label['text'] = "New Text"
my_label.config(text="New Text", font=('Helvetica', 24, 'bold'), padx=50, pady=50)
# my_label.pack()  # Will place label in the center of screen by default.
# my_label.place(x=100, y=200)  # More precise than .pack(). Too specific, though.
my_label.grid(column=0, row=0)  # Imagine your program is a grid, using cols and rows. Think it as a dataframe!

# Create buttons.
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


# Create another button.
new_button = Button(text="Click Me Too!", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry component.

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=3)

window.mainloop()  # Will keep the window on screen. Keep  this line of code at the end of the program.

