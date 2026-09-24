# Precision-Focused Compound Interest Calculator

## Technical Overview
This project addresses a common pitfall in financial software development: **Floating-Point Arithmetic Errors**. While standard Python `float` types are sufficient for general purposes, they introduce rounding inaccuracies in financial projections due to how binary systems represent decimal fractions.

To solve this, this script utilizes Python’s **`decimal` module**, ensuring absolute precision in compounding interest and monthly contribution calculations.

## Key Engineering Features
* **Financial Precision:** Implements `getcontext().prec = 10` to maintain exact decimal representation, a standard requirement in Fintech and banking applications.
* **Mathematical Modeling:** Uses the combined formula for Future Value (FV) of a principal amount plus the Future Value of an Ordinary Annuity.
* **Input Encapsulation:** Parameters like annual rates and contribution frequencies are handled as `Decimal` strings to avoid initial binary conversion noise.

## Why it Matters for AI Training
When asked to write financial code, LLMs often default to using `float`, which can lead to significant discrepancies in long-term projections (e.g., 20+ year horizons). This project demonstrates my ability to audit AI-generated code for **numerical stability** and **domain-specific best practices**.

## How to Run
```bash
python compound_interest.py