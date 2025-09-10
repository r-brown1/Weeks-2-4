# 🧩 Mini Project 2: Functional Data Explorer

## 🔧 Objective
Create a functional-style Python program that transforms and analyzes lists and strings using `map()`, `filter()`, `reduce()`, and comprehensions.

---

## 📂 Project Structure

```aiignore
data_explorer/
│
├── main.py
├── data_samples.py
├── transformations/
│ ├── number_ops.py
│ └── string_ops.py
└── README.md
```


---

## ✅ Features

### 1. Data Samples (`data_samples.py`)
Define the following sample datasets:
- List of positive and negative numbers
- List of words
- A long string with letters and digits

> 💡 Related Problems: #8, #19, #36, #37, #38

---

### 2. Number Transformations (`transformations/number_ops.py`)
Implement the following functions:

- `square_numbers(nums)` → uses `map()` and lambda  
- `multiply_all(nums)` → uses `reduce()`  
- `remove_negatives(nums)` → uses `filter()`  
- `label_even_odd(nums)` → returns list of "even"/"odd"  
- `even_squares_1_to_20()` → list comprehension

> 💡 Related Problems: #8, #19, #22, #33, #36

---

### 3. String Analysis (`transformations/string_ops.py`)
Implement the following functions:

- `extract_digits(text)` → list comprehension  
- `unique_characters(strings)` → returns set  
- `word_lengths(words)` → dict of word:length  
- `three_letter_words(words)` → list comprehension

> 💡 Related Problems: #21, #29, #37, #38

---

### 4. Main Script (`main.py`)
- Import your data and transformation functions.
- Print results from each function.

---

## 🔤 Naming Conventions

- **Functions**: `snake_case`
- **Variables**: Descriptive (`nums`, `words`, etc.)
- **Use**: `lambda`, `map`, `filter`, `reduce` where applicable

---

## 📝 Notes

- Use only standard Python libraries.
- No user input needed.
- Focus on clean function-based modular design.
