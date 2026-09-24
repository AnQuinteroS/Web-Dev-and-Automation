# Hypertrophy Macro Tracker & Data Processor

## Technical Overview
This application is a data-driven tool designed to calculate optimal macronutrient distributions for muscle hypertrophy. It focuses on **Robust Input Validation** and **Data Structuring**, ensuring that physiological constraints are respected before any computation takes place.

## Key Engineering Features
* **Defensive Programming:** Implements rigorous error handling using `try-except` blocks and `ValueError` exceptions to catch unrealistic inputs (e.g., negative weight or starvation-level caloric budgets).
* **Logical Structuring:** Outputs results using a Python **Dictionary**, allowing for easy integration with JSON APIs or front-end dashboards in a full-stack environment.
* **Algorithm Accuracy:** Applies specific biological coefficients (2.2g/kg for protein, 25% caloric fat floor) to ensure the output is scientifically grounded and logically consistent.

## Why it Matters for AI Training
AI models frequently "hallucinate" nutritional formulas or fail to implement basic safety checks on user-provided data. This project showcases my skill in **Data Sanitation** and my ability to verify that an algorithm correctly follows a provided set of logical rules without edge-case failures.

## How to Run
```bash
python hypertrophy_macros.py
```
