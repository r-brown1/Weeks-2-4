## 📁 Project 2: Pandas - Student Performance Analytics

### 🔹 Objective
Create a student performance data system that supports loading, cleaning, analyzing, and reporting using Pandas.

---

### 📌 Requirements Specification

**Description**:  
You are working for a school's analytics department to build insights from students' academic records.

#### Tasks:
1. **Load & Inspect**:
   - Load `students.csv`, inspect the first 5 rows.
2. **Create & Update DataFrame**:
   - Programmatically create a DataFrame with `Name`, `Age`, and `Grade`.
   - Add 3 new student records.
3. **Analyze**:
   - Calculate average, median, and standard deviation of `Grade`.
   - Group by `Grade` and count number of students.
   - Use `pivot_table` to get average `Age` per `Grade`.
4. **Filtering & Sorting**:
   - Filter students with `Age > 18`.
   - Sort by `Grade` descending.
5. **Missing Data**:
   - Simulate missing values in `score` column.
   - Fill missing scores with mean, then drop rows with any remaining NaNs.
6. **Merging & Concatenation**:
   - Merge DataFrames on `student_id` to include scores.
   - Concatenate two DataFrames with distinct indexes.
7. **Visualization**:
   - Plot a histogram of student scores.

#### Core Dependencies:
- `pandas>=2.0`
- `matplotlib>=3.8`

---

### 📁 Folder Structure

```
student_analytics/
│
├── data/
│ ├── students.csv # Sample student dataset
│ └── student_scores.csv # Additional dataset to merge
│
├── src/
│ ├── data_loader.py # Load and clean data
│ ├── analysis.py # Grade and age analytics
│ ├── visualization.py # Histogram plotting
│ └── merge_utils.py # Merge and concat operations
│
├── notebooks/
│ └── student_report.ipynb # Jupyter notebook for analysis
└── pd_student_perf_analytics.md
```


---

### ✅ Code Quality Criteria
- Use descriptive variable names.
- Apply function-level docstrings with type hints.
- Validate merged/joined data with assertions.
- Clean separation of logic: loading, transformation, analysis, and plotting.

---

These projects simulate real-world use cases and require mastery of foundational NumPy and Pandas operations. Each task aligns with your practice problems and expands them into full analytical workflows.

