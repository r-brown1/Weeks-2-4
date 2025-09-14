# 🧼 Real-World Mini Project: E-Commerce Product Data Cleaning

## Objective
You are working as a Data Quality Engineer for an e-commerce platform. Your task is to clean and standardize a messy product catalog (`data.csv`) to ensure consistency and reliability for downstream applications like search, pricing, and recommendation systems.

## 📁 Folder Structure

```aiignore
ecommerce_data_cleaning/
│
├── data/
│ └── data.csv # Raw input data (unmodified)
│
├── cleaned_data/
│ └── cleaned_products.csv # Cleaned output dataset
│
├── src/
│ └── cleaner.py # All data cleaning functions
│
├── main.py # Entry point to run cleaning pipeline
```

---

## 🧾 Requirements Specification

Use **only Pandas** to implement the following transformations on `data.csv`.

### 1. Load & Inspect
- Load `data.csv` using `pd.read_csv()`.
- Identify and report all missing values by column.

### 2. Missing Value Handling
- Fill missing `age` values with the mean of the column.
- Replace missing `status` values with `'Unknown'`.
- Drop rows with any remaining missing values.

### 3. Duplicate & String Cleaning
- Remove duplicate rows.
- Standardize `city` column to lowercase.
- Remove leading/trailing spaces in all string-type columns.

### 4. Type Conversion & Numeric Fixes
- Convert the `date` column to datetime using `pd.to_datetime()`.
- Round all values in the `price` column to two decimal places.
- Replace negative values in the `sales` column with 0.

### 5. Value Normalization
- Normalize `score` values to range [0, 1] (min-max scaling).
- Apply z-score normalization to the `height` column.

### 6. Outlier Detection & Flags
- Remove rows where `income` is more than 3 standard deviations from the mean.
- Create a new column `expenses_outlier` flagging rows with `expenses` above a set threshold (e.g., 10,000).
- Identify and print outliers in `salary` using IQR method.

### 7. Value Standardization
- Standardize inconsistent values in the `gender` column (e.g., convert all to `'male'` or `'female'`).
- Convert `experience` from strings like `'5 years'` to integers (`5`).

### 8. Encoding
- Apply one-hot encoding to the `department` column.
- Apply label encoding to the `grade` column (`A`, `B`, `C` → `0`, `1`, `2`).

### 9. Generalized Scaling Function
- Implement `min_max_normalize(df: pd.DataFrame) -> pd.DataFrame`:
  - Normalizes all numeric columns to [0, 1]
  - Returns the modified DataFrame

---

## 📌 Naming Conventions

| Element         | Naming Convention          |
|----------------|-----------------------------|
| Files & Folders | Lowercase with underscores  |
| Functions       | `snake_case`                |
| Variables       | `snake_case`                |
| Output file     | `cleaned_products.csv`      |

---

## ✅ Code Quality Criteria

- **Modular Design**:
  - All cleaning functions must be defined in `src/cleaner.py`.
  - `main.py` should only orchestrate the process (load, clean, save).
- **Reusable Functions**:
  - Every transformation step must be encapsulated in its own function.
  - Avoid hardcoding column names unless explicitly required.
- **Documentation**:
  - Each function must include:
    - A docstring explaining the purpose, input, and output.
    - Inline comments for non-obvious logic.
- **Data Integrity**:
  - Original input data must not be modified.
  - Cleaned dataset must be saved as `cleaned_products.csv` in `cleaned_data/`.
- **No Extra Dependencies**:
  - Only Pandas is allowed (no sklearn, numpy, etc.).

---
