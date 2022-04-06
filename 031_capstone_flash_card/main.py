from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except:
    original_data = pd.read_csv('data/german_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    """Return new card from list of words."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill='black')
    canvas.itemconfig(card_word, text=current_card['German'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer= window.after(3000, func=flip_card)


def flip_card():
    """"Change the card to show the English card for the current card, as well as the image of the card
    front to the card back."""
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    """Discard cards whose words the user already knows."""
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)

    next_card()

# --------------------------- UI SETUP ---------------------------- #
# Create window.
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Flip the cards.
flip_timer = window.after(3000, func=flip_card)

# Create canvas.
canvas = Canvas(width=800, height=526)

# Insert image into canvas.
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, font=('Helvetica', 40,'italic'))
card_word = canvas.create_text(400, 263, font=('Helvetica', 60, 'bold'))
canvas.grid(column=0,row=0, columnspan=2)

# Add two buttons.
cross_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_img, command=next_card)
unknown_button.config(
    background=BACKGROUND_COLOR,
    highlightthickness=0,
    borderwidth=0,
    relief='flat'
    )
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file='images/right.png')
known_button = Button(image=check_img, command=is_known)
known_button.config(
    background=BACKGROUND_COLOR,
    highlightthickness=0,
    borderwidth=0,
    relief='flat'
)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()