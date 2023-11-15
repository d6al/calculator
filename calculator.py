def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  if y == 0:
    raise ValueError("Cannot divide by zero")
  return x / y


def calculator():
  while True:
    print("\nCalculator Menu:")
    print("+")
    print("-")
    print("x")
    print("/")
    print("Exit")

    choice = input("Enter arithmetic function:")

    if choice == 'Exit':
      print("K. Bye!")
      break

    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

      if choice == '+':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")

      elif choice == '-':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")

      elif choice == 'x':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")

      elif choice == '/':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")

      else:
        print("Invalid choice. Please enter an arithmetic function")

    except ValueError as e:
      print(f"Error: {e}. Please enter valid numerical inputs.")

    except ZeroDivisionError:
      print(
          "Error: Cannot divide by zero. Please enter a non-zero second number."
      )


if __name__ == "__main__":
  calculator()
