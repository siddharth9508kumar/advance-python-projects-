# Basics of File Handling & Exception Handling in Python

This experiment covers two core Python concepts: **File Handling** and **Exception Handling**, implemented through 14 hands-on programs.

---

## 📂 Section 1: File Handling

All programs in this section operate on a file named `sample.txt`.

| Q# | Description | Key Concept |
|----|-------------|-------------|
| Q1 | Create a file and write text into it | `open()` with `"w"` mode, `write()`, `close()` |
| Q2 | Open and read the full content of a file | `open()` with `"r"` mode, `read()` |
| Q3 | Read and print the file line by line | `readlines()`, `for` loop |
| Q4 | Count the number of lines in a file | `len(readlines())` |
| Q5 | Count the number of words in a file | `split()`, `len()` |
| Q6 | Count the total number of characters in a file | `len(read())` |
| Q7 | Count only alphabetic characters | `isalpha()` |
| Q8 | Count vowels in a file | Membership test with `"aeiouAEIOU"` |

### Sample Outputs

```
# Q1
Work done

# Q2
welome to file handlinghello world

# Q4 — Line count
1

# Q5 — Word count
5

# Q6 — Character count
34

# Q7 — Alphabetic character count
30

# Q8 — Vowel count
11
```

---

## ⚠️ Section 2: Exception Handling

| Q# | Description | Key Concept |
|----|-------------|-------------|
| Q1 | Handle divide-by-zero without try/except | Conditional `if/else` check |
| Q2 | Handle divide-by-zero using try/except/finally | `try`, `except`, `finally` |
| Q3 | Handle a generic exception | Broad `except` clause |
| Q4 | Handle invalid input (ValueError) | `except ValueError` |
| Q5 | Handle missing file (FileNotFoundError) | `except FileNotFoundError` |
| Q6 | Use the `else` block when no exception occurs | `try/except/else` |
| Q7 | Use the `finally` block for guaranteed cleanup | `try/except/finally` |

### Sample Outputs

```
# Q1 — Without try/except
enter the first number: 2
enter the second number: 0
devide by zero error

# Q2 — With try/except/finally
enter the first number: 5
enter the second number: 0
can't devide a number by zero
Thank you

# Q4 — ValueError
enter a number: n
invalid input

# Q5 — FileNotFoundError
file not found

# Q6 — else block
file created

# Q7 — finally block
finally block
```

---

## 🧠 Concepts Covered

- File modes: `"r"` (read), `"w"` (write)
- File methods: `read()`, `readlines()`, `write()`, `close()`
- String methods: `split()`, `isalpha()`
- Exception handling: `try`, `except`, `else`, `finally`
- Built-in exceptions: `ZeroDivisionError`, `ValueError`, `FileNotFoundError`
- Defensive programming with and without `try/except`

---

## ▶️ How to Run

**Prerequisites:** Python 3.x

```bash
# Run any program directly
python q1_file_write.py

# Or run the combined experiment notebook/script
python experiment9.py
```

> **Note:** Programs in Section 1 will create/read a file called `sample.txt` in the same directory.

---

## 📁 File Structure

```
experiment-9/
├── README.md
├── sample.txt                
├── file_handling/
│   ├── q1_write.py
│   ├── q2_read.py
│   ├── q3_readlines.py
│   ├── q4_count_lines.py
│   ├── q5_count_words.py
│   ├── q6_count_chars.py
│   ├── q7_count_alpha.py
│   └── q8_count_vowels.py
└── exception_handling/
    ├── q1_no_try.py
    ├── q2_try_except.py
    ├── q3_specific_exception.py
    ├── q4_value_error.py
    ├── q5_file_not_found.py
    ├── q6_else_block.py
    └── q7_finally_block.py
```

---
