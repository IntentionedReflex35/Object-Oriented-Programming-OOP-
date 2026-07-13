# 🧠 Object-Oriented Programming (OOP) in Python — First Principles

Welcome to my Object-Oriented Programming repository!
> *A personal learning journal and code repository tracing my journey into Object-Oriented Programming through first-principles thinking.*

---

## 📖 What This Project Is

This repository is not a tutorial. It is not a course. It is a **documented learning experience**.

Every file here was written while working through Object-Oriented Programming (OOP) in Python from the ground up — starting with the '*why*' before the '*how*'. The code, structure, and comments reflect genuine learning in real time: the confusion, the clarity, the breakthroughs, and the gradual building of intuition.

If you are a beginner trying to understand OOP not just *syntactically* but *conceptually*, this repository might be the companion you were looking for.

---

## 🎯 Goals of This Project

- Understand **why OOP exists** before learning what it looks like
- Build each concept from scratch — no magic, no shortcuts
- Write code that *explains itself* — through naming and structure
- Track the mental model as it evolves, from procedural thinking to object-oriented thinking
- Create a reference I (and others) can return to at any stage

## 📁 Repository Structure

The repository is organised sequentially into dedicated modules, each focusing on a fundamental pillar of OOP:

```
Object-Oriented Programming(OOP)/
│
├── 01Python Classes and Objects/
│   ├── understanding_OOP.md     # What life looks like before objects
|    └── Dog_practice.py         # Creating objects, class attributes, methods(functions that belong to a class), constructor methods(`__init__`)
│
├── 02Encapsulation/
│   ├── understanding_Encapsulation.md       # What encapsulation looks like using ATM system as analogy
│   └── BankAccount_practice.py      # How Python enforces privacy, getter/setter method
│
├── 03Inheritance/
│   ├── understanding_Inheritance.md           # Interpretation with common traits of animals
│   └── Animal_practice.py      # Buliding a parent class,Extending and specialising through child classes, super keyword
│
├── 04Polymorphism/
│   ├── understanding_Polymorphism.md    # Same name, different behaviours
│   ├── Animal_example.py       # Making objects play nice with operators
│   └── Notification_system.py  # Another example for comprehension
│
├── 05Abstraction/
│   ├── understanding_Abstraction.md     # Internal complexity, differences between Encapsulation and Abstraction
│   └── PaymentSystem.py        # How Python approximates interfaces using ABC module
│
├── 06Real_World_projects/
│   ├── All_4_Pillars_example.py # A mini project using all four pillars
│   └── Library_System.py        # A mini project using all four pillars
│
├── notes/
│   └── glossary.md             # OOP terms in plain language
│
├── quiz/
│   ├── oop_quiz.py             # interactive quiz script
│   └── quiz_README.md          
│  
├── .gitignore
│
├── LICENSE                     # MIT LICENSE
│
└── README.md                   
```

---

## 🧱 The Four Pillars — A Beginner's Summary

| Pillar            | What It Means                                                          | Where It Lives     |
|-------------------|------------------------------------------------------------------------|--------------------|
| **Encapsulation** | Bundling data and behaviour together; hiding what shouldn't be exposed | `02Encapsulation/` |
| **Inheritance**   | Building new classes on top of existing ones                           | `03Inheritance/`   |
| **Polymorphism**  | Different objects responding to the same instruction differently       | `04Polymorphism/`  |
| **Abstraction**   | Hiding complexity behind a clean, simple interface                     | `05Abstraction/`   |

---

## 🧭 Learning Path (Recommended Reading Order)

If you are exploring this as a learning resource, follow this sequence:

```
01 → 02 → 03 → 04 → 05 → 06
```

Each folder builds on the previous. The `notes/` directory can be read at any point — especially `glossary.md` when a term is not understood clearly.

---

## 💡 First Principles Approach — What Does That Mean Here?

*First principles thinking* means refusing to accept "just memorise this syntax" as a sufficient answer.

For every concept in this project, the question asked first was:

> **"What problem does this solve, and why was it designed this way?"**

For example — before learning what a `class` is, the question was: *what happens when you don't have classes?* The answer to that question (see `01Python Classes and Objects/`) makes everything that comes after feel inevitable rather than arbitrary.

This approach takes longer. It is worth it.

---

## 🔧 Prerequisites

- Python 3.10+ installed
- A code editor (VS Code, PyCharm, or any IDE of your choice)
- Curiosity — no prior OOP knowledge required

```bash
# Clone the repository
git clone  https://github.com/IntentionedReflex35/Object-Oriented-Programming-OOP-.git

# Navigate into the project
cd Object-Oriented Programming(OOP)

# Run any file directly
python 01Python Classes and Objects/Dog_practice.py
```

No external dependencies. No `requirements.txt`. Pure Python, pure learning.

---

## 🗒️ Code Style & Conventions

The code in this repository is intentionally and mostly **verbose and over-commented**. This is not sloppy practice — it is deliberate pedagogy.

- Variable names are descriptive, sometimes even long, to make intent obvious
- Comments explain *why* a decision was made, not just *what* the line does
- Most files are self-contained and can be read independently

---

## 🤝 How This Was Made

This project was born from a personalised learning session conducted inside an IDE. Concepts were explored interactively — questions asked, code written live, misconceptions corrected in real time — and then the outputs were organised into this structured repository.

The value is not just in the code. It is in the *shape* of the learning — how the understanding was built, layer by layer, from first principles.

---

## 📚 Further Reading

Once you have worked through this project, the following resources pair well with the foundations built here:

- [Python Official Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- *Fluent Python* by Luciano Ramalho — for when you are ready to go deep
- *Clean Code* by Robert C. Martin — for writing OOP that others can maintain
- [Real Python — OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)

---

## 📄 License

This project is open source under the [MIT License](LICENSE). Use it, fork it, learn from it, share it.

---

## 🙋 About

This repository represents a personal milestone — the point where Python stopped being a scripting tool and started becoming a language for building systems. It is shared publicly in the hope that someone else at the same starting point finds it useful.

> *"The best way to learn is to build. The best way to remember is to explain."*

---

## 👨🏿‍🎓 Author

**Jeshurun Nana Kojo Ansah** — Geomatic Engineering student | Aspiring Data Analyst  
🔗 [GitHub: IntentionedReflex35](https://github.com/IntentionedReflex35)

> *"Move stealthy, execute in silence."*

---

<div align="center">

**Built with curiosity. Documented with honesty. Shared with purpose.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/github/license/IntentionedReflex35/Object-Oriented-Programming-OOP-?style=flat-square)
![Last commit](https://img.shields.io/github/last-commit/IntentionedReflex35/Object-Oriented-Programming-OOP-?style=flat-square)
![Stars](https://img.shields.io/github/stars/IntentionedReflex35/Object-Oriented-Programming-OOP-?style=flat-square)
![Approach](https://img.shields.io/badge/Approach-First%20Principles-f59e0b?style=flat-square)
![Level](https://img.shields.io/badge/Level-Beginner%20Friendly-a855f7?style=flat-square)

</div>
