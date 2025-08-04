from tkinter import *
from tkinter import Canvas, Label
from quiz_brain import QuizBrain
# Constants for the UI
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizi Fuzy")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(False, False)
        

        self.score_level = Label( text="Score: 00", bg=THEME_COLOR, fg="white", font=("Arial", 14, "bold"))
        self.score_level.grid(row=0, column=1, sticky="w")

        self.canvas = Canvas(width=300, height=400, bg="white")
        self.question_text = self.canvas.create_text(150,200, width=270,text="Quiz Question is inside this box lah, jaka naka jaka naka", fill=THEME_COLOR, font=("Arial", 20, "bold", "italic"),anchor="center", justify="center" , )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.currect_btn= Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        
        self.currect_btn.grid(row=2, column=0)
        self.wrong_btn = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_btn.grid(row=2, column=1)
        

        

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz \nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.currect_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
            return
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)


    def true_pressed(self):
       is_true = self.quiz.check_answer("True")
       self.give_feedback(is_true)
    

    def false_pressed(self):
        is_false =self.quiz.check_answer("False")
        self.give_feedback(is_false)
        
       


#For giving feedback after answering

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_level.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)

