import decimal

# Use the default precision (28 digits) to handle large capital amounts safely
# Avoid arbitrarily small precision limits (e.g., prec=10) in financial contexts.
decimal.getcontext().prec = 28

def calculate_compound_interest(principal, rate, time_years, n_compounds_per_year=1):
    """
    Calculates compound interest.
    Formula: A = P(1 + r/n)^(nt)
    """
    try:
        p = decimal.Decimal(str(principal))
        r = decimal.Decimal(str(rate))
        t = decimal.Decimal(str(time_years))
        n = decimal.Decimal(str(n_compounds_per_year))
        
        # Calculate the future amount
        amount = p * (1 + (r / n)) ** (n * t)
        
        # Quantize to 2 decimal places (standard financial output), rounding half up
        result = amount.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)
        return result
        
    except (decimal.InvalidOperation, decimal.DivisionByZero) as e:
        print(f"Error calculating interest: Invalid input values. Details: {e}")
        return None

if __name__ == "__main__":
    # Test with a large amount to ensure it processes without throwing exceptions
    large_principal = 123456789.00
    result = calculate_compound_interest(large_principal, 0.05, 10)
    if result is not None:
        print(f"Future value of ${large_principal:,.2f}: ${result:,.2f}")
