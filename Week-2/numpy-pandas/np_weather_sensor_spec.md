# Mini Project Assignment Specifications

## 📁 Project 1: NumPy - Weather Sensor Data Simulation

### 🔹 Objective
Simulate a real-world scenario where weather sensors record hourly temperature readings. You will use NumPy to process, analyze, and reshape this synthetic data.

---

### 📌 Requirements Specification

**Description**:  
You're working on an IoT-based weather monitoring system. The system collects temperature data every hour from multiple locations. Your job is to simulate and analyze this data using NumPy.

#### Tasks:
1. **Generate synthetic temperature data**:
   - Simulate hourly temperatures (in °C) for 7 days across 3 cities using a 2D NumPy array of shape `(7*24, 3)`.
2. **Reshape the data** to have shape `(7, 24, 3)` where each dimension represents `(days, hours, cities)`.
3. **Compute statistics**:
   - Mean, standard deviation, and maximum temperature per city.
   - Hour with highest average temperature across all cities.
4. **Transformations**:
   - Convert the array to Fahrenheit.
   - Normalize the temperatures (z-score normalization).
5. **Array Operations**:
   - Add Gaussian noise to simulate sensor error.
   - Perform element-wise addition and multiplication with scalar adjustments.
6. **Slicing**:
   - Extract temperatures for day 3, hours 12–18, for all cities.

#### Core Dependencies:
- `numpy>=1.24`

---

### 📁 Folder Structure

```
weather_sensor/
│
├── data/
│ └── simulated_temperature.npy
│
├── src/
│ ├── generate_data.py # Creates and saves the synthetic temperature data
│ ├── analysis.py # Contains statistical and array operations
│ └── utils.py # Helper functions (e.g., normalization, conversions)
│
├── notebooks/
│ └── weather_analysis.ipynb # Jupyter notebook demonstrating end-to-end processing
│
└── README.md
```

### ✅ Code Quality Criteria
- Follow PEP8 standards.
- Functions must include docstrings and type annotations.
- Use `assert` or simple unit tests for verifying array shapes and outputs.
- Modular function design in `utils.py`.
