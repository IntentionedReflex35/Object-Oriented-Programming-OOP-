# 🧠 OOP in Python — Interactive Quiz

A terminal-based interactive quiz that tests understanding of the four pillars of Object-Oriented Programming in Python.
Built as part of a first-principles learning journey — where the *why* always comes before the *what*.

---

## 📌 What This Is

This quiz was created after completing a full deep-dive into OOP, covering all
four pillars from scratch:

| Pillar            | Core Idea                                  |
|-------------------|--------------------------------------------|
| 🔒 Encapsulation  | Hide data. Control access.                 |
| 👨‍👧 Inheritance | Write once. Share everywhere.              |
| 🎭 Polymorphism   | Same instruction. Different behaviour.     |
| 🫙 Abstraction    | Enforce the contract. Hide the complexity. |

---

## ▶️ How to Run It

No installations. No dependencies. Just Python.

```bash
python oop_quiz.py
```

> Requires Python 3.6 or higher. Uses only standard library modules (`time`, `textwrap`).

---

## 🕹️ How It Works

Each of the 10 questions follows the same flow:

```
Question appears
      ↓
You type your answer freely in your own words
      ↓
Instant keyword-based feedback  ✔ or ⚠
      ↓
Press ENTER to reveal the full model answer
      ↓
Rate yourself honestly  →  1 / 2 / 3
      ↓
Next question
```

At the end, you get a full breakdown of your performance and a list of exactly
which questions to revisit — if any.

---

## 🎯 Rating System

| Rating | Meaning                           |
|--------|-----------------------------------|
| `1`    | Nailed it completely              |
| `2`    | Got the idea, missed some details |
| `3`    | Needs more review                 |

The final verdict is based on your self-ratings:

- **Outstanding 🏆** — zero `3`s, at most two `2`s
- **Solid 💪** — one or two `3`s
- **Keep going 🔄** — three or more `3`s

---

## 📂 File Structure

```
quiz/
  oop_quiz.py     ← the quiz script
  README.md       ← this file
```

---

## 🔍 What's Inside the Code

The script is organized into four clear layers:

```
① Data        →  questions list (10 dicts, each with question, keywords, model_answer)
② Helpers     →  slow_print, check_answer, divider, press_enter
③ Screens     →  show_welcome, show_question, get_user_answer,
                  show_feedback, self_rate, show_results
④ Main guard  →  run_quiz() called only when file is run directly
```

### Key design decisions worth noting

**Keyword scanning** — answers are checked against a list of concept keywords per question. Hitting at least 2 keywords
triggers a ✔. This keeps feedback honest without requiring exact phrasing.

```python
hits = sum(1 for kw in keywords if kw.lower() in answer_lower)
return hits >= 2
```

**`textwrap.wrap()`** — model answers are word-wrapped at 70 characters for clean terminal display, regardless of 
screen size.

```python
for line in textwrap.wrap(q['model_answer'], width=70):
    slow_print(f" {line}", delay=0.035)
```

**Main guard** — the script uses the standard `if __name__ == "__main__":` pattern, meaning `run_quiz()` only fires 
when the file is run directly. Any future script that imports a function from this file won't accidentally trigger
a full quiz session.

```python
if __name__ == "__main__":
    run_quiz()
```

---

## 📝 Questions Covered

1. What was the core problem with code BEFORE OOP existed?
2. What is a Class and what is an Object?
3. What is `self` and why does every method need it?
4. What is Encapsulation and why do we need it?
5. What problem does Inheritance solve?
6. What does `super()` do and when would you use it?
7. What is Polymorphism and what problem does it solve?
8. Why is Polymorphism MORE powerful at large scale?
9. What is Abstraction and how is it different from Encapsulation?
10. How do all 4 pillars work TOGETHER?

---

## 🔖 GitHub Issue

This file was tracked under a GitHub Issue for deeper review and enhancement.
The issue has since been resolved — a feature branch was created, changes were
made, a pull request was opened, and the issue was closed upon merge.

---

## 💡 Context

This quiz is part of a larger OOP learning repository built on a first-principles philosophy: understand the *problem* 
before the *solution*, and always ask *why* before *what*. The same repository includes a `Library Management System` 
project that implements all four pillars in a single working codebase.
