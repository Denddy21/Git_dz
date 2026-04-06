try:
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    result = num_1 / num_2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid numeric value.")
else:
    print(f"Result is: {result}")
finally:
    print("Calculation process finished.")
