# -------------------------------------------------------
#             OOP IN PYTHON — INTERACTIVE Q&A QUIZ
#         Based on a first-principles learning session
# -------------------------------------------------------

import time
import textwrap

# Colours for the terminal aesthetics
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RESET = "\033[0m"
YELLOW = "\033[93m"

# ------ Questions & Answers Data -------
# All questions are stored in a list. Each question is accompanied by a model answer.
# Each question is stored as a dictionary in the "questions" list.
questions = [
    {
        "number": 1,
        "question": "What was the core problem with code BEFORE OOP existed?",
        "keywords": ["floating", "repeat", "loose", "tamper", "group", "unprotect", "relation", "variable"],
        "model_answer": (
            "Before OOP, data was just floating around as loose variables with no "
            "grouping or relationship between them. For example, student1_name, "
            "student1_age, and student1_grade all belong together but nothing in "
            "the code knew that. This also meant data was unprotected — anyone "
            "could accidentally or intentionally tamper with it."
        ),
    },
    {
        "number": 2,
        "question": "What is a Class and what is an Object? What is the relationship between them?",
        "keywords": ["blueprint", "template", "instance", "object", "real", "stamp", "recipe", "unique"],
        "model_answer": (
            "A Class is a blueprint or template — like a recipe or architectural plan. "
            "It defines what something IS (its attributes and methods) but it is not "
            "the thing itself. An Object is the actual thing created FROM that blueprint "
            "— like a house built from a plan, or a cake baked from a recipe. "
            "Each object is independent and holds its own unique data."
        ),
    },
    {
        "number": 3,
        "question": "What is 'self' and why does every method inside a class need it?",
        "keywords": ["self", "object", "specific", "which", "current", "refer", "instance", "who"],
        "model_answer": (
            "self refers to the specific object that called the method. When you have "
            "two dogs — Bruno and Bella — and you call bark() on both, Python needs to "
            "know WHICH dog is barking each time. self is Python automatically passing "
            "in the object itself so the method knows whose data to use. "
            "dog1.bark() means self = dog1. dog2.bark() means self = dog2."
        ),
    },
    {
        "number": 4,
        "question": "What is Encapsulation and why do we need it? Give a real example.",
        "keywords": ["private", "protect", "hide", "access", "tamper", "bank", "control", "__"],
        "model_answer": (
            "Encapsulation means hiding internal data and controlling how it is accessed "
            "from outside. Without it, anyone can directly change sensitive data — like "
            "setting a bank balance to -99999 with no checks. By making the balance "
            "private (__balance) and only allowing access through methods like deposit() "
            "and withdraw(), we enforce rules and protect the data from invalid changes."
        ),
    },
    {
        "number": 5,
        "question": "What problem does Inheritance solve and how does it work?",
        "keywords": ["repeat", "common", "parent", "child", "inherit", "share", "once", "dry"],
        "model_answer": (
            "Inheritance solves the problem of repetition. When multiple classes share "
            "common behaviour — like Dog, Cat and Bird all eating and sleeping — writing "
            "those methods in every class separately is wasteful. With Inheritance, a "
            "parent class (Animal) holds the common behaviour, and child classes inherit "
            "it for free while adding their own unique behaviour on top."
        ),
    },
    {
        "number": 6,
        "question": "What does super() do and when would you use it?",
        "keywords": ["parent", "super", "keep", "extend", "build", "add", "on top", "inherit"],
        "model_answer": (
            "super() lets a child class call the parent's version of a method and then "
            "build on top of it. Instead of completely replacing the parent's behaviour, "
            "the child says 'do what the parent does first, then I'll add my own twist.' "
            "For example, a Dog can call super().eat() to keep the parent's eating "
            "behaviour and then add 'begs for more food' on top."
        ),
    },
    {
        "number": 7,
        "question": "What is Polymorphism and what problem does it solve?",
        "keywords": ["same", "different", "form", "if", "elif", "method", "open", "closed", "extend"],
        "model_answer": (
            "Polymorphism means 'many forms' — the same instruction produces different "
            "behaviour depending on the object receiving it. It solves the problem of "
            "giant if/elif chains where every new type requires editing existing code. "
            "With Polymorphism, each class handles its own behaviour, and your core "
            "logic never needs to change when new types are added — following the "
            "Open/Closed Principle: open for extension, closed for modification."
        ),
    },
    {
        "number": 8,
        "question": "Why is Polymorphism MORE powerful at a large scale than small scale?",
        "keywords": ["team", "git", "merge", "conflict", "spaghetti", "scale", "branch", "isolated"],
        "model_answer": (
            "At small scale, if/elif is fine. But as software grows with teams of "
            "developers, the if/elif approach creates spaghetti code that only the "
            "original author understands. Multiple developers editing the same function "
            "causes Git merge conflicts. With Polymorphism, each developer works in "
            "their own isolated class file — no conflicts, no stepping on each other's "
            "work, and the core logic stays untouched no matter how many types are added."
        ),
    },
    {
        "number": 9,
        "question": "What is Abstraction and how is it DIFFERENT from Encapsulation?",
        "keywords": ["enforce", "contract", "abstract", "hide", "complex", "ABC", "must", "interface"],
        "model_answer": (
            "Abstraction enforces a contract — it forces child classes to implement "
            "required methods using @abstractmethod. If a child forgets, Python throws "
            "an error immediately. It also hides internal complexity so users only see "
            "what they need (like pressing one button on a phone). The difference: "
            "Encapsulation PROTECTS data from being tampered with. "
            "Abstraction HIDES complexity and ENFORCES structure."
        ),
    },
    {
        "number": 10,
        "question": "How do all 4 pillars of OOP work TOGETHER? Why do they complement each other?",
        "keywords": ["encapsulation", "inherit", "polymorphism", "abstract", "together", "depend", "pillar",
                     "complement"],
        "model_answer": (
            "No pillar is a standalone — they build on each other naturally. "
            "Encapsulation protects data inside each class. Inheritance eliminates "
            "repetition by sharing common behaviour. Polymorphism lets each child "
            "handle shared methods in its own way, keeping core logic clean. "
            "Abstraction enforces the contract so every child follows the rules. "
            "Together they produce systems that are protected, non-repetitive, "
            "extensible, and enforced."
        ),
    },
]


# ------------ FUNCTIONS FOR THE QUIZ ----------------------------
#     -----------     HELPERS     -----------
def slow_print(text, delay=0.015):
    """Print text character by character for a typewriter effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def check_answer(user_answer, keywords):
    """Check if user answer contains enough keyword hits."""
    answer_lower = user_answer.lower()
    hits = sum(1 for kw in keywords if kw.lower() in answer_lower)
    return hits >= 2          # at least 2 keyword concepts touched


def divider():
    print(f"\n{CYAN}{'─' * 62}{RESET}\n")


def press_enter(prompt="  Press ENTER to continue..."):
    input(f"\n{YELLOW}{prompt}{RESET}")


# ----------------- SCREENS  ------------------------
def show_welcome():
    slow_print(f"{BOLD}{CYAN}  ╔══════════════════════════════════════════════════════╗{RESET}")
    slow_print(f"{BOLD}{CYAN}  ║         OOP IN PYTHON — INTERACTIVE QUIZ             ║{RESET}")
    slow_print(f"{BOLD}{CYAN}  ║         All 4 Pillars · 10 Questions                 ║{RESET}")
    slow_print(f"{BOLD}{CYAN}  ╚══════════════════════════════════════════════════════╝{RESET}")

    print()
    print(f"  How it works:\n")
    print(f"  {YELLOW}①{RESET}  Read the question carefully")
    print(f"  {YELLOW}②{RESET}  Type your answer in your own words and hit ENTER")
    print(f"  {YELLOW}③{RESET}  See instant feedback — then the model answer reveals")
    print(f"  {YELLOW}④{RESET}  Rate yourself honestly before moving on\n")
    press_enter("  Ready? Press ENTER to start the quiz...")


def show_question(q, index, total):
    divider()
    print(f"  {BOLD}Question {index} of {total}{RESET}")
    print()
    slow_print(f"  {BOLD}{q['question']}{RESET}", delay=0.02)


def get_user_answer():
    lines = []
    print(f"  {YELLOW}Your answer:{RESET}")
    print(f"  {CYAN}(Type your answer. Press ENTER twice when done){RESET}\n")
    while True:
        line = input(" > ")
        if line == "" and lines:
            break
        if line != "":
            lines.append(line)
    return ' '.join(lines)


show_welcome()
show_question(questions[0], 1, 10)
get_user_answer()
show_question(questions[1], 2, 10)
get_user_answer()


# show feedback after user answer to verify with model answer
show_question(questions[2], 3, 10)
user_answer = get_user_answer()
q = questions[2]
passed = check_answer(user_answer, q["keywords"])
if passed:
    slow_print(f"  {GREEN}{BOLD}✔  Good answer! You hit the key concepts.{RESET}")
else:
    slow_print(f"  {YELLOW}{BOLD}⚠  Partially there — check the model answer below.{RESET}")
# reveal model answer
press_enter("  Press ENTER to reveal the model answer...")

print()
slow_print(f"  {BOLD}Model Answer:{RESET}", delay=0.02)
print()
# print(q['model_answer'])

# Word wrapping for model answer
wrapped_text = textwrap.fill(q['model_answer'], width=70)
lines = wrapped_text.split('\n')
for line in lines:
    slow_print(f" {line}", delay=0.03)
