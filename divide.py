def divide(a, b):
  """
  Returns the quotient of two numbers.
  Handles division by zero.
  """
  if b == 0:
    return "Error: Cannot divide by zero"
  return a / b