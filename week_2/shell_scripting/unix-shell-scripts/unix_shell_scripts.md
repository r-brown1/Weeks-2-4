# Mini Project: UNIX Shell Scripting Practice

## Objective
Develop a series of 20 standalone shell scripts implementing core UNIX shell scripting concepts such as file manipulation, loops, conditionals, variables, functions, and text processing utilities (`cut`, `sed`, `awk`, `grep`). This project aims to solidify your understanding of shell scripting fundamentals through practical tasks.

---

## Project Requirements Specification

### 1. Folder Structure & Naming Conventions

```aiignore
unix-shell-scripts/
│
├── 01_backup_txt_files.sh
├── 02_rename_log_to_bak.sh
├── 03_greeting_variable.sh
├── 04_check_file_exists.sh
├── 05_count_lines.sh
├── 06_sum_function.sh
├── 07_list_py_files.sh
├── 08_while_loop_numbers.sh
├── 09_check_create_dir.sh
├── 10_delete_old_files.sh
├── 11_append_files.sh
├── 12_uppercase_conversion.sh
├── 13_ls_grep_sh.sh
├── 14_cut_second_column.sh
├── 15_sed_replace_foo_bar.sh
├── 16_awk_filter_column.sh
├── 17_print_name_age.sh
├── 18_count_files.sh
├── 19_greet_user_function.sh
├── 20_word_count_pipe.sh
└── README.md
```

---

### 2. Core Dependencies
- **Shell:** Bash (compatible with `#!/bin/bash` or `#!/bin/sh` where applicable)
- Common UNIX utilities: `cp`, `mv`, `test` or `[ ]`, `echo`, `ls`, `grep`, `cut`, `sed`, `awk`, `cat`, `wc`
- No external packages or dependencies outside typical UNIX/Linux environments

---

### 3. Function Implementation Details
- Each script should be **executable** (`chmod +x`)
- Scripts should start with the proper shebang line (`#!/bin/bash`)
- Each script should:
  - Handle input arguments properly (with validation when applicable)
  - Use clear and consistent variable naming (uppercase for constants/readonly variables, lowercase or camelCase for variables)
  - Include comments explaining major steps and logic
- Scripts involving functions should declare them with clear names, use `local` variables inside functions when appropriate, and demonstrate function calls.
- Scripts should use appropriate quoting (`""` or `''`) to prevent globbing or word splitting issues.
- Use idiomatic shell scripting best practices for conditionals and loops.

---

### 4. Code Quality Criteria
- **Readability:** Clear, concise code with consistent indentation (2 or 4 spaces)
- **Robustness:** Proper error handling for missing arguments, non-existent files/directories
- **Portability:** Use POSIX-compliant syntax where possible (unless otherwise specified)
- **Efficiency:** Avoid unnecessary commands or subshells
- **Documentation:** Include header comments in each script with:
  - Script purpose
  - Usage example
  - Author and date (optional)

---

### 5. Submission Deliverables
- A zipped folder named `unix-shell-practice.zip` containing the entire folder structure with scripts
- A `README.md` summarizing:
  - How to run each script
  - Any assumptions made
  - Notes on functionality or limitations

---

### Example Script Header Template
```
#!/bin/bash
# Script: 01_backup_txt_files.sh
# Description: Creates a directory 'backup' and copies all '.txt' files into it.
# Usage: ./01_backup_txt_files.sh
# Author: Your Name
# Date: YYYY-MM-DD


This project provides a solid foundation in shell scripting and prepares you for real-world automation tasks. Enjoy coding!
```