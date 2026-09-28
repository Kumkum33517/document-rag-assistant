import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pipeline import ask

# (question, keywords, any one of which should appear in the answer)
TESTS = [
    ("How many books can a student borrow at once?", ["4", "four"]),
    ("What is the fine for returning a book late?", ["5"]),
    ("How many times can a book be renewed?", ["twice", "two", "2"]),
    ("What are the reading room timings on weekdays?", ["8", "10"]),
    ("How much does alumni membership cost?", ["1000"]),
    ("Who is the president of the United States?", ["could not find"]),
]

passed = 0
for q, keywords in TESTS:
    answer, _ = ask(q)
    ok = any(k.lower() in answer.lower() for k in keywords)
    passed += ok
    print(f"[{'PASS' if ok else 'FAIL'}] {q}\n    -> {answer.strip()}\n")

print(f"{passed}/{len(TESTS)} passed")
