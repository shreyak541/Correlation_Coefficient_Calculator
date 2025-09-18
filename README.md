# Correlation Coefficient Calculator

This Python script calculates the **Pearson correlation coefficient (r)** between two sets of data points.

---

## What Is a Correlation Coefficient?

The correlation coefficient `r` measures the strength and direction of the **linear relationship** between two variables:

- `r = 1` → Perfect positive correlation  
- `r = -1` → Perfect negative correlation  
- `r = 0` → No linear correlation  

---

## How It Works

1. Prompts the user for the number of data points (`n ≥ 2`).  
2. Collects two lists of values: `x` and `y`.  
3. Computes sums needed for the Pearson formula: `sum(x)`, `sum(y)`, `sum(x*y)`, `sum(x^2)`, `sum(y^2)`.  
4. Calculates the Pearson correlation coefficient using the following plain-text formula (GitHub-friendly):

```
	  n * sum(x*y) - sum(x) * sum(y)
r = ---------------------------------------------
	sqrt([n * sum(x^2) - (sum(x))^2] * [n * sum(y^2) - (sum(y))^2])
```

5. Handles invalid input and cases where division by zero occurs.  
6. Prints the correlation coefficient up to 4 decimal places.

---

## How to Run

Save the file as `correlation_coefficient_calculator.py` and run:

```bash
python correlation_coefficient_calculator.py
