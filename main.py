# This script imports and uses the functions from the calculator files.

from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

# Define two numbers to perform operations on
num1 = 10
num2 = 5

# Perform the operations and print the results
print(f"Adding {num1} and {num2}: {add(num1, num2)}")
print(f"Subtracting {num1} and {num2}: {subtract(num1, num2)}")
print(f"Multiplying {num1} and {num2}: {multiply(num1, num2)}")
print(f"Dividing {num1} and {num2}: {divide(num1, num2)}")

# Test the division by zero case
print("\n--- Testing division by zero ---")
num3 = 0
print(f"Dividing {num1} by {num3}: {divide(num1, num3)}")