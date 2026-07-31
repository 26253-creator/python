import tkinter as tk
from tkinter import messagebox
import random


# ---------------- QUESTION DATABASE ---------------- #

questions = [

    {
        "question": "Simplify: 3x + 5x",
        "options": ["8x", "15x", "8", "3x"],
        "answer": "8x"
    },

    {
        "question": "Solve: x + 6 = 14",
        "options": ["6", "8", "10", "20"],
        "answer": "8"
    },

    {
        "question": "Expand: 3(x + 4)",
        "options": [
            "3x + 4",
            "3x + 12",
            "x + 12",
            "12x"
        ],
        "answer": "3x + 12"
    },

    {
        "question": "Factorise: x² + 5x",
        "options": [
            "x(x + 5)",
            "x(x - 5)",
            "5x",
            "x²"
        ],
        "answer": "x(x + 5)"
    },

    {
        "question": "The solution to x - 4 = 10 is x = 14.",
        "options": [
            "True",
            "False"
        ],
        "answer": "True"
    },

    {
        "question": "Simplify: 7a - 3a",
        "options": [
            "4a",
            "10a",
            "21a",
            "a"
        ],
        "answer": "4a"
    },

    {
        "question": "Solve: 2x = 18",
        "options": [
            "7",
            "8",
            "9",
            "10"
        ],
        "answer": "9"
    },

    {
        "question": "Expand: 5(y + 2)",
        "options": [
            "5y + 10",
            "y + 10",
            "10y",
            "5y + 2"
        ],
        "answer": "5y + 10"
    },

    {
        "question": "Substitute x = 3 into 2x + 4",
        "options": [
            "6",
            "8",
            "10",
            "12"
        ],
        "answer": "10"
    },

    {
        "question": "Factorise: 4x + 8",
        "options": [
            "4(x + 2)",
            "2(x + 4)",
            "x(4 + 8)",
            "4x"
        ],
        "answer": "4(x + 2)"
    },

    {
        "question": "Simplify: 9m + 2m",
        "options": [
            "11m",
            "18m",
            "9m",
            "7m"
        ],
        "answer": "11m"
    },

    {
        "question": "Solve: x - 8 = 12",
        "options": [
            "4",
            "20",
            "12",
            "8"
        ],
        "answer": "20"
    },

    {
        "question": "Expand: 2(a + 7)",
        "options": [
            "2a + 14",
            "a + 14",
            "14a",
            "2a + 7"
        ],
        "answer": "2a + 14"
    },

    {
        "question": "Factorise: 6x + 18",
        "options": [
            "6(x + 3)",
            "3(x + 6)",
            "x(6 + 18)",
            "6x"
        ],
        "answer": "6(x + 3)"
    },

    {
        "question": "Simplify: 4x + 3 - x",
        "options": [
            "3x + 3",
            "5x",
            "4x + 2",
            "x + 3"
        ],
        "answer": "3x + 3"
    },

    {
        "question": "Solve: 3x = 21",
        "options": [
            "5",
            "6",
            "7",
            "8"
        ],
        "answer": "7"
    },

    {
        "question": "Substitute y = 5 into 3y + 2",
        "options": [
            "15",
            "17",
            "20",
            "10"
        ],
        "answer": "17"
    },

    {
        "question": "The expression 2x + 3x can be simplified to 5x.",
        "options": [
            "True",
            "False"
        ],
        "answer": "True"
    },

    {
        "question": "Expand: 4(x + 5)",
        "options": [
            "4x + 20",
            "4x + 5",
            "x + 20",
            "20x"
        ],
        "answer": "4x + 20"
    },

    {
        "question": "Solve: x ÷ 4 = 5",
        "options": [
            "9",
            "20",
            "10",
            "15"
        ],
        "answer": "20"
    }

]


# ---------------- QUIZ APPLICATION ---------------- #

class QuizApp(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Year 9 Algebra Quiz")
        self.geometry("900x600")
        self.resizable(False, False)


        self.current_question = 0
        self.score = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.skipped_questions = 0
        self.attempted_questions = 0


        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)


        self.show_home()



    # Clear current page

    def clear_screen(self):

        for widget in self.container.winfo_children():
            widget.destroy()



    # ---------------- HOME PAGE ---------------- #

    def show_home(self):

        self.clear_screen()


        title = tk.Label(
            self.container,
            text="Year 9 Algebra Quiz",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=80)



        info = tk.Label(
            self.container,
            text="20 Questions\n\nSimplifying Expressions\nSolving Equations\nExpanding Brackets\nFactorising\nSubstitution",
            font=("Arial", 18)
        )

        info.pack()



        start_button = tk.Button(
            self.container,
            text="START QUIZ",
            font=("Arial", 20),
            width=15,
            command=self.start_quiz
        )

        start_button.pack(pady=50)



    # ---------------- START QUIZ ---------------- #

    def start_quiz(self):

        random.shuffle(questions)

        self.current_question = 0
        self.score = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.skipped_questions = 0
        self.attempted_questions = 0


        self.show_question()
            # ---------------- QUESTION PAGE ---------------- #

    def show_question(self):

        self.clear_screen()


        if self.current_question >= len(questions):

            self.show_end()
            return


        q = questions[self.current_question]


        question_number = tk.Label(
            self.container,
            text=f"Question {self.current_question + 1} / {len(questions)}",
            font=("Arial", 18)
        )

        question_number.pack(pady=20)



        question_text = tk.Label(
            self.container,
            text=q["question"],
            font=("Arial", 26),
            wraplength=700
        )

        question_text.pack(pady=40)



        self.answer = tk.StringVar()



        for option in q["options"]:

            button = tk.Radiobutton(
                self.container,
                text=option,
                variable=self.answer,
                value=option,
                font=("Arial", 18)
            )

            button.pack(pady=5)



        button_frame = tk.Frame(self.container)
        button_frame.pack(pady=40)



        submit_button = tk.Button(
            button_frame,
            text="Submit Answer",
            font=("Arial", 16),
            width=15,
            command=self.check_answer
        )

        submit_button.grid(row=0, column=0, padx=20)



        skip_button = tk.Button(
            button_frame,
            text="Skip Question",
            font=("Arial", 16),
            width=15,
            command=self.skip_question
        )

        skip_button.grid(row=0, column=1, padx=20)




    # ---------------- CHECK ANSWER ---------------- #

    def check_answer(self):

        selected = self.answer.get()


        if selected == "":

            messagebox.showwarning(
                "No Answer",
                "Please select an answer or skip the question."
            )

            return



        correct_answer = questions[self.current_question]["answer"]


        self.attempted_questions += 1



        if selected == correct_answer:

            self.correct_answers += 1
            self.score += 1


            messagebox.showinfo(
                "Correct!",
                "✓ Correct answer!"
            )


        else:

            self.incorrect_answers += 1


            messagebox.showinfo(
                "Incorrect",
                f"✗ Incorrect answer.\n\nCorrect answer: {correct_answer}"
            )



        self.current_question += 1


        self.show_question()


    # ---------------- SKIP QUESTION ---------------- #

    def skip_question(self):

        self.skipped_questions += 1


        messagebox.showinfo(
            "Skipped",
            "Question skipped."
        )


        self.current_question += 1


        self.show_question()





    # ---------------- END PAGE ---------------- #

    def show_end(self):

        self.clear_screen()

        percentage = (self.score / len(questions)) * 100

        if percentage >= 90:

            grade = "Excellence"


        elif percentage >= 70:

            grade = "Merit"


        elif percentage >= 50:

            grade = "Achieved"


        else:

            grade = "Not Achieved"

        title = tk.Label(
            self.container,
            text="Quiz Complete!",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=40)




        result = tk.Label(
            self.container,
            text=f"""
Final Results

Score: {self.score}/{len(questions)}

Percentage: {percentage:.0f}%

Grade: {grade}


Correct: {self.correct_answers}

Incorrect: {self.incorrect_answers}

Skipped: {self.skipped_questions}

Attempted: {self.attempted_questions}
""",
            font=("Arial", 20)
        )

        result.pack()

        retry_button = tk.Button(
            self.container,
            text="Retry Quiz",
            font=("Arial", 18),
            width=15,
            command=self.start_quiz
        )

        retry_button.pack(pady=20)


        quit_button = tk.Button(
            self.container,
            text="Quit",
            font=("Arial", 18),
            width=15,
            command=self.destroy
        )

        quit_button.pack()





# ---------------- RUN PROGRAM ---------------- #

app = QuizApp()

app.mainloop()
