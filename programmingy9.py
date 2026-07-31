import tkinter as tk
from tkinter import messagebox
import random

# -----------------------
# Question Bank
# -----------------------

questions = [
    {"question": "Solve: x + 6 = 14",
     "options": ["6", "8", "10", "20"],
     "answer": "8"},

    {"question": "The solution to x - 4 = 10 is x = 14.",
     "tf": True,
     "answer": "True"},

    {"question": "Simplify: 3x + 2x",
     "options": ["5", "6x", "5x", "x"],
     "answer": "5x"},

    {"question": "2x + 3x = 5x",
     "tf": True,
     "answer": "True"},

    {"question": "Solve: 2x = 18",
     "options": ["8", "9", "16", "20"],
     "answer": "9"},

    {"question": "Simplify: 7x - 2x",
     "options": ["5x", "9x", "5", "x"],
     "answer": "5x"},

    {"question": "The expression 4x + 2 can be simplified to 6x.",
     "tf": True,
     "answer": "False"},

    {"question": "Solve: x ÷ 3 = 5",
     "options": ["2", "8", "15", "18"],
     "answer": "15"},

    {"question": "Evaluate: 2x + 3 when x = 4",
     "options": ["8", "11", "14", "15"],
     "answer": "11"},

    {"question": "Expand: 3(x + 2)",
     "options": ["3x + 2", "3x + 6", "x + 6", "6x"],
     "answer": "3x + 6"},

    {"question": "Factorise: 5x + 10",
     "options": ["5(x + 2)", "10(x + 5)", "5(x + 10)", "x(5+10)"],
     "answer": "5(x + 2)"},

    {"question": "3 × 4x = 12x",
     "tf": True,
     "answer": "True"},

    {"question": 'Which expression means "five more than x"?',
     "options": ["5x", "x - 5", "x + 5", "5 ÷ x"],
     "answer": "x + 5"},

    {"question": "Solve: 4x = 24",
     "options": ["4", "5", "6", "8"],
     "answer": "6"},

    {"question": "If x = 3, then x² = 9.",
     "tf": True,
     "answer": "True"},

    {"question": "Solve: 4x + 5 = 2x + 19",
     "options": ["5", "6", "7", "8"],
     "answer": "7"},

    {"question": "Solve: 5x - 8 = 2x + 13",
     "options": ["5", "6", "7", "8"],
     "answer": "7"},

    {"question": "Solve: 3x + 12 = x + 26",
     "options": ["5", "6", "7", "8"],
     "answer": "7"},

    {"question": "Cinema booking fee question",
     "options": ["4x + 5 = 29", "4x - 5 = 29", "5x + 4 = 29", "29x = 9"],
     "answer": "4x + 5 = 29"},

    {"question": "Mia wallet question",
     "options": ["7x + 7 = 42", "42x = 7", "7x = 42", "x + 42 = 7"],
     "answer": "7x + 7 = 42"}
]

# -----------------------
# Quiz Setup
# -----------------------

quiz_questions = random.sample(questions, 10)

current_question = 0
correct = 0
incorrect = 0
attempted = 0
skipped = 0

# -----------------------
# Functions
# -----------------------

def start_quiz():
    start_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    load_question()

def load_question():
    global current_question

    if current_question >= len(quiz_questions):
        show_results()
        return

    q = quiz_questions[current_question]

    question_label.config(
        text=f"Question {current_question + 1}/10\n\n{q['question']}"
    )

    for widget in option_frame.winfo_children():
        widget.destroy()

    answer_var.set("")

    if q.get("tf"):
        choices = ["True", "False"]
    else:
        choices = q["options"]

    for choice in choices:
        rb = tk.Radiobutton(
            option_frame,
            text=choice,
            variable=answer_var,
            value=choice,
            font=("Arial", 12)
        )
        rb.pack(anchor="w")

def submit_answer():
    global current_question, correct, incorrect, attempted

    selected = answer_var.get()

    if selected == "":
        messagebox.showwarning(
            "No Answer",
            "Please select an answer or press Skip."
        )
        return

    attempted += 1

    if selected == quiz_questions[current_question]["answer"]:
        correct += 1
    else:
        incorrect += 1

    current_question += 1
    load_question()

def skip_question():
    global current_question, skipped

    skipped += 1
    current_question += 1
    load_question()

def show_results():
    quiz_frame.pack_forget()

    if attempted > 0:
        percentage = (correct / attempted) * 100
    else:
        percentage = 0

    if percentage >= 90:
        grade = "EXCELLENCE"
        message = "Outstanding work!"
    elif percentage >= 75:
        grade = "MERIT"
        message = "Great effort!"
    elif percentage >= 50:
        grade = "ACHIEVED"
        message = "Good job!"
    else:
        grade = "NOT ACHIEVED"
        message = "Keep practising Algebra."

    result_text = f"""
Correct: {correct}
Incorrect: {incorrect}
Attempted: {attempted}
Skipped: {skipped}

Score: {percentage:.1f}%

Grade: {grade}

{message}
"""

    results_label.config(text=result_text)

    results_frame.pack(fill="both", expand=True)

def restart_quiz():
    root.destroy()

# -----------------------
# GUI
# -----------------------

root = tk.Tk()
root.title("Year 9 Algebra Quiz")
root.geometry("700x500")

# Start Screen
start_frame = tk.Frame(root)

title = tk.Label(
    start_frame,
    text="Year 9 Algebra Quiz",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

info = tk.Label(
    start_frame,
    text="You will be given 10 random Algebra questions.\n"
         "You may answer or skip questions.\n"
         "Your grade will be shown at the end.",
    font=("Arial", 12)
)
info.pack(pady=10)

start_button = tk.Button(
    start_frame,
    text="Start Quiz",
    command=start_quiz,
    width=20
)
start_button.pack(pady=20)

start_frame.pack(fill="both", expand=True)

# Quiz Screen
quiz_frame = tk.Frame(root)

question_label = tk.Label(
    quiz_frame,
    font=("Arial", 14),
    wraplength=600
)
question_label.pack(pady=20)

answer_var = tk.StringVar()

option_frame = tk.Frame(quiz_frame)
option_frame.pack()

submit_button = tk.Button(
    quiz_frame,
    text="Submit",
    command=submit_answer,
    width=15
)
submit_button.pack(pady=10)

skip_button = tk.Button(
    quiz_frame,
    text="Skip",
    command=skip_question,
    width=15
)
skip_button.pack()

# Results Screen
results_frame = tk.Frame(root)

results_label = tk.Label(
    results_frame,
    font=("Arial", 14)
)
results_label.pack(pady=20)

retry_button = tk.Button(
    results_frame,
    text="Close Quiz",
    command=restart_quiz,
    width=20
)
retry_button.pack(pady=20)

root.mainloop()
