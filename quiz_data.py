"""Load and manage quiz question data from text files."""

from __future__ import annotations

import os
import random
from dataclasses import dataclass
from typing import Literal

QuestionType = Literal["multiple_choice", "true_false", "word_problem"]

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.txt")
ATTEMPTED_FILE = os.path.join(DATA_DIR, "attempted.txt")
NOT_ATTEMPTED_FILE = os.path.join(DATA_DIR, "not_attempted.txt")


@dataclass
class Question:
    qid: int
    qtype: QuestionType
    prompt: str
    options: list[str]
    answer: str
    secondary_answer: str | None = None


def load_questions() -> list[Question]:
    questions: list[Question] = []
    with open(QUESTIONS_FILE, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            qid = int(parts[0])
            qtype = parts[1]
            prompt = parts[2]
            if qtype == "multiple_choice":
                options = parts[3:-1]
                answer = parts[-1]
                questions.append(Question(qid, qtype, prompt, options, answer))
            elif qtype == "true_false":
                answer = parts[3]
                questions.append(
                    Question(qid, qtype, prompt, ["True", "False"], answer)
                )
            elif qtype == "word_problem":
                answer = parts[3]
                secondary = parts[4] if len(parts) > 4 else None
                questions.append(
                    Question(qid, qtype, prompt, [], answer, secondary)
                )
    return questions


def read_id_file(path: str) -> list[int]:
    ids: list[int] = []
    if not os.path.exists(path):
        return ids
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            ids.append(int(line))
    return ids


def write_id_file(path: str, ids: list[int]) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("# Question IDs for the current quiz session (one per line)\n")
        for qid in ids:
            handle.write(f"{qid}\n")


def reset_tracking_files(all_question_ids: list[int]) -> None:
    write_id_file(ATTEMPTED_FILE, [])
    write_id_file(NOT_ATTEMPTED_FILE, list(all_question_ids))


def mark_attempted(qid: int) -> None:
    attempted = read_id_file(ATTEMPTED_FILE)
    not_attempted = read_id_file(NOT_ATTEMPTED_FILE)
    if qid not in attempted:
        attempted.append(qid)
    if qid in not_attempted:
        not_attempted.remove(qid)
    write_id_file(ATTEMPTED_FILE, attempted)
    write_id_file(NOT_ATTEMPTED_FILE, not_attempted)


def select_random_questions(
    questions: list[Question], count: int = 10
) -> list[Question]:
    return random.sample(questions, min(count, len(questions)))


def normalise_answer(value: str) -> str:
    return value.strip().lower().replace(" ", "")
