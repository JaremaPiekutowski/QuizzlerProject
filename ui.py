from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        """Initialize quiz interface"""
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,
                           padx=20,
                           pady=20)
        self.canvas = Canvas(width=300,
                             height=250,
                             bg="white",
                             highlightthickness=0)
        self.canvas.grid(row=1,
                         column=0,
                         columnspan=2,
                         padx=20,
                         pady=20)
        self.score_label = Label(text=f"Score: {self.quiz.score}",
                                 fg="white",
                                 bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Custom question",
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image,
                                   highlightthickness=0,
                                   bd=0,
                                   padx=20,
                                   pady=20,
                                   command=self.check_if_false)
        self.false_button.grid(row=2, column=0)
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image,
                                  highlightthickness=0,
                                  bd=0,
                                  padx=20,
                                  pady=20,
                                  command=self.check_if_true)
        self.true_button.grid(row=2, column=1)
        self.display_next_question()
        self.window.mainloop()

    def display_next_question(self):
        """Display next question or finish the game"""
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.display_final_score()

    def display_final_score(self):
        """Display final score"""
        self.canvas.itemconfig(self.question_text, text=f"""YOU'VE COMPLETED THE QUIZ!\n
                  Your final score was {self.quiz.score}/{len(self.quiz.question_list)}""")
        self.window.after(4000, func=self.window.destroy)

    def display_winning(self):
        """Display an info showing that the player selected the right answer"""
        self.canvas.itemconfig(self.question_text, text="You're right!")
        self.score_label.config(text=f"Score: {self.quiz.score}",
                                fg="white",
                                bg=THEME_COLOR)
        self.window.after(2000, func=self.display_next_question)

    def display_losing(self):
        """Display an info showing that the player selected the wrong answer"""
        self.canvas.itemconfig(self.question_text, text="You're wrong!")
        self.window.after(2000, func=self.display_next_question)

    def check_if_true(self):
        """Check if the True answer is right or wrong"""
        # THE REASON I DIDN'T MAKE ONE FUNCTION WITH AN ARGUMENT "True" OR "False" IS BECAUSE A TKINTER
        # REQUIREMENT - A COMMAND FUNCTION FOR A BUTTON MUST NOT CONTAIN ARGUMENTS. OR AM I WRONG? (KH)
        if self.quiz.check_answer("True"):
            self.display_winning()
        else:
            self.display_losing()

    def check_if_false(self):
        """Check if the False answer is right or wrong"""
        if self.quiz.check_answer("False"):
            self.display_winning()
        else:
            self.display_losing()
