def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        try:
            result = num / denom
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both inputs must be numeric values."