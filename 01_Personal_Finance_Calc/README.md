# Precision-Focused Compound Interest Calculator

## Technical Overview
This project addresses a common pitfall in financial software development: **Floating-Point Arithmetic Errors**. While standard Python `float` types are sufficient for general purposes, they introduce rounding inaccuracies in financial projections due to how binary systems represent decimal fractions.

To solve this, this script utilizes Python’s **`decimal` module**, ensuring absolute precision in compounding interest and monthly contribution calculations.

## Key Engineering Features
* **Financial Precision:** Uses `getcontext().prec = 28` and rounds the final result to cents with `ROUND_HALF_UP`, a standard requirement in Fintech and banking applications.
* **Mathematical Modeling:** Implements the compound interest formula $A = P(1 + r/n)^{nt}$ with a configurable number of compounding periods per year.
* **Input Encapsulation:** Every input is converted to `Decimal` through `str()` to avoid binary conversion noise, and invalid values (including zero compounding periods) are handled without crashing.

## Why it Matters for AI Training
When asked to write financial code, LLMs often default to using `float`, which can lead to significant discrepancies in long-term projections (e.g., 20+ year horizons). This project demonstrates my ability to audit AI-generated code for **numerical stability** and **domain-specific best practices**.

## How to Run
```bash
python compound_interest.py
```
