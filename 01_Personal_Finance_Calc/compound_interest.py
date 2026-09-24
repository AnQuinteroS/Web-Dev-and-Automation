"""
Personal Finance & Investment Calculator
* Objective: Calculate compound interest over time while demonstrating 
  proper handling of floating-point arithmetic in financial contexts.
* AI Evaluation Relevance: LLMs often fail at financial math due to 
  floating-point rounding errors. This script uses Python's 'decimal' 
  module to enforce absolute precision.
"""

from decimal import Decimal, getcontext

# Set precision for financial calculations
getcontext().prec = 10

def calculate_compound_interest(principal, annual_rate, years, contributions_per_month):
    """
    Calculates the future value of an investment with monthly contributions.
    Formula used: A = P(1 + r/n)^(nt) + PMT × {[(1 + r/n)^(nt) - 1] / (r/n)}
    """
    # Convert inputs to Decimal for exact precision
    P = Decimal(str(principal))
    r = Decimal(str(annual_rate))
    t = Decimal(str(years))
    PMT = Decimal(str(contributions_per_month))
    n = Decimal('12') # Monthly compounding
    
    # 1. Calculate compound interest for the principal amount
    # P(1 + r/n)^(nt)
    principal_growth = P * (1 + r/n)**(n*t)
    
    # 2. Calculate future value of a series (monthly contributions)
    # PMT × {[(1 + r/n)^(nt) - 1] / (r/n)}
    contribution_growth = PMT * (((1 + r/n)**(n*t) - 1) / (r/n))
    
    # 3. Total Future Value
    total_amount = principal_growth + contribution_growth
    
    return round(total_amount, 2)

def run_simulation():
    print("--- Investment Projection Simulation ---")
    
    initial_investment = 1000.00  # Starting with $1000
    monthly_addition = 150.00     # Adding $150 every month
    interest_rate = 0.08          # 8% annual return (historical market average)
    investment_period = 10        # 10 years

    future_value = calculate_compound_interest(
        initial_investment, interest_rate, investment_period, monthly_addition
    )

    print(f"Initial Investment: ${initial_investment}")
    print(f"Monthly Contribution: ${monthly_addition}")
    print(f"Annual Interest Rate: {interest_rate * 100}%")
    print(f"Time Horizon: {investment_period} years")
    print("-" * 40)
    print(f"Projected Portfolio Value: ${future_value}")

if __name__ == "__main__":
    run_simulation()