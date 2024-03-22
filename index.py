def perform_operation(operation, numbers):
  """Performs the given arithmetic operation on a list of numbers."""
  if operation == 'add':
      return sum(numbers)
  elif operation == 'subtract':
      result = numbers[0]
      for num in numbers[1:]:
          result -= num
      return result
  elif operation == 'multiply':
      result = 1
      for num in numbers:
          result *= num
      return result
  elif operation == 'divide':
      result = numbers[0]
      for num in numbers[1:]:
          if num == 0:
              return "Error: Division by zero is not allowed."
          result /= num
      return result

# Example usage:
def get_user_input():
  """Collects user's choice and numbers for calculation."""
  choice = input("Enter choice (1/2/3/4/5): ")
  if choice in ('1', '2', '3', '4'):
      numbers = input("Enter numbers separated by space: ")
      numbers = [float(num) for num in numbers.split()]
      return choice, numbers
  return choice, []

# Improved Main Program Loop with clearer structure and input handling
operations = { '1': 'add', '2': 'subtract', '3': 'multiply', '4': 'divide' }

while True:
  print("\nSelect operation:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")

  choice, numbers = get_user_input()

  # Exit the program if the user chooses to
  if choice == '5':
      print("Exiting the program. Goodbye!")
      break
  elif choice in operations:
      result = perform_operation(operations[choice], numbers)
      print(f"Result: {result}")
  else:
      print("Invalid Input. Please enter a number between 1 and 5.")
