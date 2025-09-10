# 🧩 Mini Project 1: Personal Data Toolkit

## 🔧 Objective
Build a small toolkit to manage and interact with personal data such as names, ages, hobbies, and scores using fundamental Python data structures and functions.

---

## 📂 Project Structure

```aiignore
personal_data_toolkit/
│
├── main.py
├── data/
│ └── students.py
├── utils/
│ ├── info_utils.py
│ └── hobby_utils.py
└── README.md
```


---

## ✅ Features

### 1. Store Personal Data (`data/students.py`)
Define a list of dictionaries where each dictionary contains:
- `name`
- `age`
- `score`

> 💡 Related Problems: #10, #23

---

### 2. Information Utilities (`utils/info_utils.py`)

Functions to implement:
- `get_average_age(student_list)` → float  
- `get_score_summary(student_list)` → dict with `min`, `max`, `avg`
- `filter_high_scores(student_dict, threshold=70)` → list of names

> 💡 Related Problems: #23, #24, #26

---

### 3. Hobby Management (`utils/hobby_utils.py`)

- Create a dictionary mapping names to lists of hobbies.
- Function: `add_hobby(name, hobby)` → adds a hobby to the person's list.

> 💡 Related Problem: #13

---

### 4. Main Script (`main.py`)
- Import and use the above functions.
- Display outputs with `print()`.
- Add a hobby for one person and show the updated list.

---

## 🔤 Naming Conventions

- **Files/Folders**: `snake_case`
- **Functions**: `snake_case`
- **Variables**: Descriptive (e.g., `student_list`, `average_score`)
- **Constants**: `UPPER_CASE`

---

## 📝 Notes

- Keep it simple — no CLI or GUI.
- Use basic error handling (e.g., missing keys, empty data).
- Follow clean code practices.
