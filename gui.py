from tkinter import *

# ---------------- QUESTIONS ---------------- #

questions = [
    {"question": "Solve: x + 6 = 20",
     "options": ["6", "8", "10", "20"],
     "answer": "8"},

    {"question": "The solution to x - 4 = 10 is x = 14.",
     "tf": True,
     "answer": "True"},
C
    {"question": "Simplify: 3x + 3x",
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

    {"question": "A cinema charges a booking fee of $5 plus $4 per ticket. The total cost came to $29. What equation could be used?",
     "answer": "4x + 5 = 29"},

    {"question": "Mia has $7 in her wallet. She earns the same amount each day. In one week she has $42. What equation could be used?",
     "answer": "7x + 7 = 42"}
]

# ---------------- VARIABLES ---------------- #

current_question = 0
score = 0

# ---------------- WINDOW ---------------- #

root = Tk()
root.title("Year 9 Algebra Quiz")
root.geometry("700x500")
root.config(bg="#dceeff")

title = Label(root,
              text="Year 9 Algebra Quiz",
              font=("Arial", 22, "bold"),
              bg="#dceeff")
title.pack(pady=20)

question_label = Label(root,
                       text="",
                       wraplength=600,
                       font=("Arial", 16),
                       bg="#dceeff")
question_label.pack(pady=20)

answer_var = StringVar()

radio_buttons = []

entry = Entry(root, font=("Arial", 16), width=30)

feedback = Label(root,
                 text="",
                 font=("Arial", 14),
                 bg="#dceeff")
feedback.pack(pady=10)

# ---------------- FUNCTIONS ---------------- #

def show_question():

    global current_question

    answer_var.set("")
    feedback.config(text="")
    entry.pack_forget()

    for button in radio_buttons:
        button.destroy()

    radio_buttons.clear()

    if current_question >= len(questions):
        finish_quiz()
        return

    q = questions[current_question]

    question_label.config(
        text=f"Question {current_question+1}\n\n{q['question']}"
    )

    if "options" in q:

        for option in q["options"]:
            rb = Radiobutton(root,
                             text=option,
                             variable=answer_var,
                             value=option,
                             font=("Arial", 14),
                             bg="#dceeff")

            rb.pack(anchor="w", padx=80)

            radio_buttons.append(rb)

    elif "tf" in q:

        for option in ["True", "False"]:
            rb = Radiobutton(root,
                             text=option,
                             variable=answer_var,
                             value=option,
                             font=("Arial", 14),
                             bg="#dceeff")

            rb.pack(anchor="w", padx=80)

            radio_buttons.append(rb)

    else:
        entry.delete(0, END)
        entry.pack()


def next_question():

    global current_question
    global score

    q = questions[current_question]

    if "answer" not in q:
        return

    if "options" in q or "tf" in q:
        user_answer = answer_var.get()
    else:
        user_answer = entry.get()

    if user_answer.strip().lower() == q["answer"].strip().lower():
        score += 1

    current_question += 1

    show_question()


def finish_quiz():

    question_label.config(
        text=f"Quiz Finished!\n\nFinal Score\n{score}/{len(questions)}"
    )

    for button in radio_buttons:
        button.destroy()

    entry.pack_forget()
    next_button.pack_forget()

# ---------------- BUTTON ---------------- #

next_button = Button(root,
                     text="Next",
                     font=("Arial", 14),
                     command=next_question)

next_button.pack(pady=20)

show_question()

root.mainloop()
