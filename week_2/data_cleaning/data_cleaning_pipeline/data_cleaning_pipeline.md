# Mini Project: Real-World Data Cleaning Pipeline

---

## Project Overview

This mini project guides you through creating a robust data cleaning pipeline for tabular datasets using Python and Pandas. The project combines multiple common real-world data cleaning tasks into a modular, maintainable codebase. Your goal is to implement reusable functions for each cleaning step, enabling flexible data preprocessing workflows.

---

## Project Requirements

### Core Dependencies

- Python 3.8+
- pandas
- numpy
- scikit-learn (for LabelEncoder)
- Optional: Jupyter Notebook for exploratory testing

### Folder Structure & Naming Conventions

```aiignore
data_cleaning_pipeline/
│
├── data/
│ └── data.csv # Raw dataset input file
│
├── src/
│ ├── init.py # Makes src a package
│ ├── data_loader.py # Functions to load and inspect data
│ ├── cleaning.py # Data cleaning function implementations
│ ├── feature_engineering.py # Functions for encoding and transformations
│ └── utils.py # Helper functions (e.g., outlier detection)
│
├── tests/
│ ├── test_cleaning.py # Unit tests for cleaning functions
│ └── test_feature_engineering.py
│
├── notebooks/
│ └── EDA_and_cleaning.ipynb # Exploratory data analysis & demo
│
├── requirements.txt # Dependency list
├── README.md
└── main.py # Script to run the full cleaning pipeline
```


---

## Functional Specifications

You will implement the following functions in `src/cleaning.py` and `src/feature_engineering.py`:

| Function Name                 | Description                                                                                 | Input                | Output              |
|------------------------------|---------------------------------------------------------------------------------------------|----------------------|---------------------|
| `load_data(filepath: str)`    | Load CSV into DataFrame, identify missing values                                            | CSV filepath (str)   | DataFrame           |
| `fill_missing_with_mean(df, col)` | Fill missing values in numeric column with column mean                                    | DataFrame, col name  | DataFrame           |
| `drop_rows_with_missing(df)` | Drop any row containing missing values                                                     | DataFrame            | DataFrame           |
| `fill_missing_with_value(df, col, value)` | Fill missing values in specified column with a given value                               | DataFrame, col, val  | DataFrame           |
| `remove_duplicates(df)`       | Identify and remove duplicate rows                                                         | DataFrame            | DataFrame           |
| `standardize_case(df, col)`   | Convert all string values in a column to lowercase                                         | DataFrame, col       | DataFrame           |
| `convert_to_datetime(df, col)`| Convert a column to datetime format                                                        | DataFrame, col       | DataFrame           |
| `round_column(df, col, decimals)` | Round numeric column values to specified decimals                                         | DataFrame, col, int  | DataFrame           |
| `normalize_gender(df, col)`   | Replace inconsistent gender labels with standardized values (e.g., 'M', 'Male', 'male')     | DataFrame, col       | DataFrame           |
| `strip_spaces(df, cols)`      | Remove leading/trailing spaces from string columns                                         | DataFrame, list[str] | DataFrame           |
| `min_max_scale(df, col)`      | Normalize column values to range [0,1]                                                     | DataFrame, col       | DataFrame           |
| `z_score_standardize(df, col)`| Apply z-score standardization to a column                                                  | DataFrame, col       | DataFrame           |
| `detect_outliers_iqr(df, col)`| Detect outliers based on IQR method                                                        | DataFrame, col       | Series (bool mask)  |
| `remove_outliers_std(df, col, n_std)` | Remove rows where values deviate more than n standard deviations                          | DataFrame, col, int  | DataFrame           |
| `flag_outliers(df, col, threshold)` | Create boolean flag column indicating outliers based on threshold                         | DataFrame, col, float| DataFrame           |
| `replace_negatives_with_zero(df, col)` | Replace negative values in a numeric column with zero                                    | DataFrame, col       | DataFrame           |
| `one_hot_encode(df, col)`     | Convert categorical column into one-hot encoded columns                                    | DataFrame, col       | DataFrame           |
| `label_encode(df, col)`       | Convert categorical labels into numeric using LabelEncoder                                 | DataFrame, col       | DataFrame           |
| `extract_numeric_years(df, col)`| Extract integers from strings like '2 years', '5 years'                                  | DataFrame, col       | DataFrame           |
| `min_max_scale_all_numeric(df)`| Standardize all numeric columns using min-max scaling                                     | DataFrame            | DataFrame           |

---

## Code Quality Criteria

- **Modularity:** Each function should perform one specific task.
- **Type hints and docstrings:** Provide clear type annotations and docstrings.
- **Error handling:** Validate inputs and raise informative exceptions.
- **Reusability:** Functions should work on any appropriate DataFrame/column.
- **Testing:** Unit tests covering normal and edge cases.
- **PEP8 compliance:** Follow Python style guidelines.
- **Logging:** Use logging to record major processing steps (optional for bonus).

---

## Deliverables

- Fully implemented Python modules under `src/`
- Unit tests in `tests/` with at least 80% code coverage
- Example notebook demonstrating cleaning pipeline on `data/data.csv`
- `main.py` script to run the entire cleaning pipeline end-to-end
- `README.md` explaining project structure, setup, and usage

---

This mini project replicates typical data cleaning workflows seen in real data science and engineering roles, focusing on clear, maintainable, and testable code.

Good luck! Feel free to ask for help with any function implementation or test design.

---

