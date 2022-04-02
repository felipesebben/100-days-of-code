from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    """Start count down timer."""
    global reps
    # Increase reps by 1.
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN  * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If we are on the 1st/3rd/5th/7th/ repetition:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Rest!", font=(FONT_NAME, 40, 'bold'), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break!", font=(FONT_NAME, 40, 'bold'), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="Work!", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    "Count down the remaining time."

    count_min = math.floor(count / 60)  # Return the minute as an integer
    count_sec = count % 60  # Return the remainder of a minute, that is, the seconds.
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # Use the .after() method to call a particular function after a particular amount of time that you stipulate.
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


# Create canvas.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Insert image into canvas.
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(102, 132, text='00:00', fill='white', font=(FONT_NAME, 27, 'bold'))
canvas.grid(column=1, row=1)

# Move count_down after the canvas, otherwise we'll get an error.

# TODO 1. Create "Timer" label.
title_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# TODO 2. Create "Start" button".
start_button = Button(
    text="Start",
    font=('Helvetica', 10, 'normal'),
    highlightthickness=0,
    command=start_timer
    )
start_button.grid(column=0, row=2)

# TODO 3. Create "Check" label.
check_marks = Label(font=(FONT_NAME, 12, 'bold'), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# TODO 4. Create "Reset" button.
reset_button = Button(text="Reset", font=('Helvetica', 10, 'normal'), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()

