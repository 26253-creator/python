import tkinter as tk
from tkinter import messagebox
import random


# ---------------- QUESTION DATABASE ---------------- #

ALL_QUESTIONS = [
    {"question": "Simplify: 3x + 5x", "options": ["8x", "15x", "8", "3x"], "answer": "8x"},
    {"question": "Solve: x + 6 = 14", "options": ["6", "8", "10", "20"], "answer": "8"},
    {"question": "Expand: 3(x + 4)", "options": ["3x + 4", "3x + 12", "x + 12", "12x"], "answer": "3x + 12"},
    {"question": "Factorise: x² + 5x", "options": ["x(x + 5)", "x(x - 5)", "5x", "x²"], "answer": "x(x + 5)"},
    {"question": "The solution to x - 4 = 10 is x = 14.", "options": ["True", "False"], "answer": "True"},
    {"question": "Simplify: 7a - 3a", "options": ["4a", "10a", "21a", "a"], "answer": "4a"},
    {"question": "Solve: 2x = 18", "options": ["7", "8", "9", "10"], "answer": "9"},
    {"question": "Expand: 5(y + 2)", "options": ["5y + 10", "y + 10", "10y", "5y + 2"], "answer": "5y + 10"},
    {"question": "Substitute x = 3 into 2x + 4", "options": ["6", "8", "10", "12"], "answer": "10"},
    {"question": "Factorise: 4x + 8", "options": ["4(x + 2)", "2(x + 4)", "x(4 + 8)", "4x"], "answer": "4(x + 2)"},
    {"question": "Simplify: 9m + 2m", "options": ["11m", "18m", "9m", "7m"], "answer": "11m"},
    {"question": "Solve: x - 8 = 12", "options": ["4", "20", "12", "8"], "answer": "20"},
    {"question": "Expand: 2(a + 7)", "options": ["2a + 14", "a + 14", "14a", "2a + 7"], "answer": "2a + 14"},
    {"question": "Factorise: 6x + 18", "options": ["6(x + 3)", "3(x + 6)", "x(6 + 18)", "6x"], "answer": "6(x + 3)"},
    {"question": "Simplify: 4x + 3 - x", "options": ["3x + 3", "5x", "4x + 2", "x + 3"], "answer": "3x + 3"},
    {"question": "Solve: 3x = 21", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Substitute y = 5 into 3y + 2", "options": ["15", "17", "20", "10"], "answer": "17"},
    {"question": "The expression 2x + 3x can be simplified to 5x.", "options": ["True", "False"], "answer": "True"},
    {
        "question": "Word Problem:\n\nA cinema charges a booking fee of $5 plus $4 per ticket.\nThe total cost came to $29.\n\nWhat equation could be used?\n(Then work out how many tickets were bought.)",
        "type": "entry",
        "answer": "4x + 5 = 29",
    },
    {
        "question": "Word Problem:\n\nMia has $7 in her wallet.\nShe earns the same amount each day.\nAfter one week she has $42.\n\nWhat equation could be used?\n(Then work out how much she earns each day.)",
        "type": "entry",
        "answer": "7x + 7 = 42",
    },
]


# ---------------- STYLE ---------------- #

BG = "#FFFFFF"
NAVY = "#0A248A"
BLUE = "#80D0F6"
PALE_BLUE = "#CFEFFF"
PURPLE = "#6078F8"
PURPLE_DARK = "#1511B8"
TEXT = "#0A248A"
SOFT_GREY = "#EAF1F6"


# ---------------- UI HELPERS ---------------- #

def rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1,
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


class RoundedButton(tk.Canvas):
    def __init__(
        self,
        parent,
        text,
        command,
        width=500,
        height=86,
        bg=PURPLE,
        fg=PURPLE_DARK,
        font=("Arial", 28, "bold"),
        border=None,
        border_width=2,
    ):
        super().__init__(parent, width=width, height=height, bg=BG, highlightthickness=0, cursor="hand2")
        self.command = command
        self.normal_bg = bg
        self.hover_bg = self._lighten(bg)
        self.fg = fg
        self.border = border
        self.border_width = border_width

        self.shape = rounded_rectangle(
            self,
            3,
            3,
            width - 3,
            height - 3,
            radius=25,
            fill=bg,
            outline=border if border else bg,
            width=border_width,
        )
        self.label = self.create_text(width / 2, height / 2, text=text, fill=fg, font=font)

        self.bind("<Button-1>", self._click)
        self.bind("<Enter>", self._enter)
        self.bind("<Leave>", self._leave)
        self.tag_bind(self.shape, "<Button-1>", self._click)
        self.tag_bind(self.label, "<Button-1>", self._click)

    @staticmethod
    def _lighten(hex_color):
        hex_color = hex_color.lstrip("#")
        r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        r = min(255, int(r + (255 - r) * 0.12))
        g = min(255, int(g + (255 - g) * 0.12))
        b = min(255, int(b + (255 - b) * 0.12))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _click(self, _event=None):
        self.command()

    def _enter(self, _event=None):
        self.itemconfigure(self.shape, fill=self.hover_bg)

    def _leave(self, _event=None):
        self.itemconfigure(self.shape, fill=self.normal_bg)


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Year 9 Maths Quiz")
        self.geometry("1000x760")
        self.minsize(900, 680)
        self.configure(bg=BG)

        self.quiz_questions = []
        self.current_question = 0
        self.score = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.skipped_questions = 0
        self.attempted_questions = 0
        self.answer = tk.StringVar()

        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True)

        self.show_home()

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def draw_question_icon(self, canvas, cx, cy, size=55):
        canvas.create_oval(cx - size, cy - size, cx + size, cy + size, outline=BLUE, width=8)
        canvas.create_arc(
            cx - size - 15,
            cy - size - 15,
            cx + size + 15,
            cy + size + 15,
            start=280,
            extent=250,
            style="arc",
            outline=BLUE,
            width=7,
        )
        canvas.create_text(cx, cy - 3, text="?", fill=BLUE, font=("Arial", 52, "bold"))

    def header_card(self, text, font_size=44):
        card = tk.Canvas(self.container, width=820, height=150, bg=BG, highlightthickness=0)
        card.pack(pady=(55, 15))
        rounded_rectangle(card, 80, 18, 800, 135, radius=20, fill=BG, outline=BLUE, width=5)
        self.draw_question_icon(card, 80, 76, size=45)
        card.create_text(445, 76, text=text, fill=NAVY, font=("Arial", font_size, "bold"))
        return card

    # ---------------- HOME PAGE ---------------- #
    def show_home(self):
        self.clear_screen()
        self.header_card("Year 9 Maths Quiz", 43)

        start_button = RoundedButton(
            self.container,
            text="Start",
            command=self.start_quiz,
            width=510,
            height=108,
            bg=PURPLE,
            fg=PURPLE_DARK,
            font=("Arial", 38, "bold"),
        )
        start_button.pack(pady=(0, 24))

        subtitle = tk.Label(
            self.container,
            text="10 algebra questions",
            bg=BG,
            fg=NAVY,
            font=("Arial", 18),
        )
        subtitle.pack(pady=(2, 12))

        topics = tk.Label(
            self.container,
            text="Simplifying  •  Equations  •  Expanding  •  Factorising  •  Substitution",
            bg=BG,
            fg="#3553A4",
            font=("Arial", 14),
        )
        topics.pack()

    # ---------------- START QUIZ ---------------- #
    def start_quiz(self):
        # 1. Separate MC questions (first 18) and entry questions (last 2)
        mc_pool = ALL_QUESTIONS[:-2]
        word_problems = ALL_QUESTIONS[-2:]

        # 2. Pick 8 random multiple-choice questions
        mc_selection = random.sample(mc_pool, 8)

        # 3. Combine them so the 2 word problems are ALWAYS questions 9 and 10
        self.quiz_questions = mc_selection + word_problems

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

        if self.current_question >= len(self.quiz_questions):
            self.show_end()
            return

        q = self.quiz_questions[self.current_question]
        self.answer = tk.StringVar()

        top = tk.Frame(self.container, bg=BG)
        top.pack(fill="x", padx=55, pady=(32, 8))

        # Mini icon
        icon = tk.Canvas(top, width=68, height=68, bg=BG, highlightthickness=0)
        icon.pack(side="left")
        self.draw_question_icon(icon, 34, 34, size=24)

        tk.Label(
            top,
            text=f"Question {self.current_question + 1}",
            bg=BG,
            fg=NAVY,
            font=("Arial", 27, "bold"),
        ).pack(side="left", padx=12)

        tk.Label(
            top,
            text=f"{self.current_question + 1} / {len(self.quiz_questions)}",
            bg=BG,
            fg="#5C72B6",
            font=("Arial", 16, "bold"),
        ).pack(side="right", padx=5)

        progress = tk.Canvas(self.container, height=18, bg=BG, highlightthickness=0)
        progress.pack(fill="x", padx=62, pady=(0, 22))
        progress.update_idletasks()
        w = max(progress.winfo_width(), 700)
        rounded_rectangle(progress, 0, 3, w, 15, radius=8, fill=SOFT_GREY, outline=SOFT_GREY)
        progress_width = w * (self.current_question / len(self.quiz_questions))
        if progress_width > 8:
            rounded_rectangle(progress, 0, 3, progress_width, 15, radius=8, fill=BLUE, outline=BLUE)

        question_card = tk.Frame(self.container, bg=PALE_BLUE, bd=0, padx=35, pady=28)
        question_card.pack(fill="x", padx=70, pady=(0, 20))

        question_font = 21 if q.get("type") == "entry" else 26
        tk.Label(
            question_card,
            text=q["question"],
            bg=PALE_BLUE,
            fg="#111111",
            font=("Arial", question_font, "bold" if not q.get("type") else "normal"),
            wraplength=790,
            justify="center",
        ).pack()

        answer_area = tk.Frame(self.container, bg=BG)
        answer_area.pack(fill="both", expand=True, padx=90)

        if q.get("type") == "entry":
            tk.Label(
                answer_area,
                text="Type the equation below:",
                bg=BG,
                fg=NAVY,
                font=("Arial", 16, "bold"),
            ).pack(pady=(10, 8))

            answer_entry = tk.Entry(
                answer_area,
                textvariable=self.answer,
                font=("Arial", 22),
                justify="center",
                relief="solid",
                bd=2,
                highlightthickness=2,
                highlightbackground=PURPLE_DARK,
                highlightcolor=PURPLE_DARK,
            )
            answer_entry.pack(ipady=12, ipadx=12, fill="x", padx=90, pady=(0, 15))
            answer_entry.focus_set()
            answer_entry.bind("<Return>", lambda _e: self.check_answer())
        else:
            options_frame = tk.Frame(answer_area, bg=BG)
            options_frame.pack(pady=(2, 10))

            for index, option in enumerate(q["options"]):
                rb = tk.Radiobutton(
                    options_frame,
                    text=option,
                    variable=self.answer,
                    value=option,
                    bg=BG,
                    fg=NAVY,
                    activebackground=BG,
                    activeforeground=NAVY,
                    selectcolor=PALE_BLUE,
                    font=("Arial", 19, "bold"),
                    indicatoron=True,
                    anchor="w",
                    padx=18,
                    pady=10,
                )
                rb.grid(row=index // 2, column=index % 2, sticky="ew", padx=24, pady=8)
            options_frame.grid_columnconfigure(0, minsize=310)
            options_frame.grid_columnconfigure(1, minsize=310)

        controls = tk.Frame(self.container, bg=BG)
        controls.pack(pady=(5, 28))

        RoundedButton(
            controls,
            text="Submit",
            command=self.check_answer,
            width=270,
            height=72,
            bg=PURPLE,
            fg=PURPLE_DARK,
            font=("Arial", 22, "bold"),
        ).pack(side="left", padx=10)

        RoundedButton(
            controls,
            text="Skip",
            command=self.skip_question,
            width=210,
            height=72,
            bg=PALE_BLUE,
            fg=NAVY,
            font=("Arial", 20, "bold"),
            border=BLUE,
        ).pack(side="left", padx=10)

    # ---------------- ANSWER CHECKING ---------------- #
    @staticmethod
    def normalise_entry(value):
        return "".join(value.lower().split())

    def check_answer(self):
        selected = self.answer.get().strip()

        if not selected:
            messagebox.showwarning("No Answer", "Please choose or type an answer, or use Skip.")
            return

        correct_answer = self.quiz_questions[self.current_question]["answer"]
        self.attempted_questions += 1

        is_entry = self.quiz_questions[self.current_question].get("type") == "entry"
        if is_entry:
            is_correct = self.normalise_entry(selected) == self.normalise_entry(correct_answer)
        else:
            is_correct = selected == correct_answer

        if is_correct:
            self.correct_answers += 1
            self.score += 1
            messagebox.showinfo("Correct!", "Correct answer!")
        else:
            self.incorrect_answers += 1
            messagebox.showinfo("Incorrect", f"Incorrect answer.\n\nCorrect answer: {correct_answer}")

        self.current_question += 1
        self.show_question()

    def skip_question(self):
        self.skipped_questions += 1
        self.current_question += 1
        self.show_question()

    # ---------------- END PAGE ---------------- #
    def show_end(self):
        self.clear_screen()

        percentage = (self.score / len(self.quiz_questions)) * 100
        if percentage >= 90:
            grade = "Excellence"
        elif percentage >= 70:
            grade = "Merit"
        elif percentage >= 50:
            grade = "Achieved"
        else:
            grade = "Not Achieved"

        score_card = tk.Canvas(self.container, width=850, height=190, bg=BG, highlightthickness=0)
        score_card.pack(pady=(70, 8))
        rounded_rectangle(score_card, 100, 20, 825, 165, radius=18, fill=BG, outline=BLUE, width=5)
        self.draw_question_icon(score_card, 100, 92, size=48)
        score_card.create_text(
            470,
            92,
            text=f"score {self.score}/{len(self.quiz_questions)}",
            fill=NAVY,
            font=("Arial", 42, "bold"),
        )

        grade_canvas = tk.Canvas(self.container, width=610, height=82, bg=BG, highlightthickness=0)
        grade_canvas.pack(pady=(0, 6))
        rounded_rectangle(grade_canvas, 10, 8, 600, 72, radius=22, fill=PALE_BLUE, outline=PALE_BLUE)
        grade_canvas.create_text(
            305,
            40,
            text=f"grade: {grade}",
            fill="#111111",
            font=("Arial", 23),
        )

        retry = RoundedButton(
            self.container,
            text="try again",
            command=self.start_quiz,
            width=540,
            height=112,
            bg=PURPLE,
            fg=PURPLE_DARK,
            font=("Arial", 39, "bold"),
        )
        retry.pack(pady=(0, 20))

        details = tk.Label(
            self.container,
            text=f"Correct: {self.correct_answers}     Incorrect: {self.incorrect_answers}     Skipped: {self.skipped_questions}",
            bg=BG,
            fg="#53659C",
            font=("Arial", 13),
        )
        details.pack(pady=(2, 8))

        quit_link = tk.Label(
            self.container,
            text="Quit",
            bg=BG,
            fg=NAVY,
            font=("Arial", 14, "underline"),
            cursor="hand2",
        )
        quit_link.pack()
        quit_link.bind("<Button-1>", lambda _e: self.destroy())


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()