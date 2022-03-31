from tkinter import *


def miles_to_km():
    number = float(miles_input.get())
    km_value = round(number * 1.609)
    result_label.config(text=f"{km_value}")

# Make window.

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=150)
window.config(padx=20, pady=20)

# Make components

# 1. Entry

miles_input = Entry(width=5)
print(miles_input.get())
miles_input.grid(column=1, row=0)

# 2. "Miles" label.
miles_label = Label(text="Miles", font=('Helvetica', 10, 'normal'), padx=20, pady=20)
miles_label.grid(column=2, row=0)


# 3. "is equal to" label.
is_equal_label = Label(text="is equal to", font=('Helvetica', 10, 'normal'), padx=20, pady=20)
is_equal_label.grid(column=0, row=1)

# 4. Result label.
result_label = Label(text="0", font=('Helvetica', 10, 'normal'), padx=20, pady=20)
result_label.grid(column=1, row=1)

# 5. "Km" label.
km_label = Label(text="Km", font=('Helvetica', 10, 'normal'), padx=20, pady=20)
km_label.grid(column=2, row=1)

# 6. "Calculate" Button
calculate_button = Button(
    text="Calculate",
    font=('Helvetica', 10, 'normal'),
    width=5,
    height=1,
    command=miles_to_km,
    padx=20,
    pady=20)
calculate_button.grid(column=1, row=2)





window.mainloop()