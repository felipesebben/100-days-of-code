from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question text",
            fill=THEME_COLOR,
            width=280,
            justify='center',
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(
            image=true_image,
            command=self.true_pressed,
            highlightthickness=0,
            borderwidth=0
        )
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(
            image=false_image,
            command=self.false_pressed,
            highlightthickness=0,
            borderwidth=0
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Call the quiz's next question."""
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        """Command for 'true' button."""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Command for 'false' button."""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Return a feedback regarding the user's input."""
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        # Use .after() to define how many milliseconds we want to delay the time by.
        self.window.after(1000, self.get_next_question)  # Get rid of the (), as it is used as input
