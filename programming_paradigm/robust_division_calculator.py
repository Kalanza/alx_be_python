def safe_divide(numerator, denominator):
 try:
    num = float(numerator)
    denom = float(denominator)

    try:
        X = num / denom
        return f"The result of the division is {X}" 
    except ZeroDivisionError:
          return "Error: Cannot divide by zero."

 except ValueError:
        return "Error: Please enter numeric values only."