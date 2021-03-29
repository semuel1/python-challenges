# Version with rounding and checking validity of the operation first.
def get_numbers():
  number1 = float(input("What is number 1? "))
  number2 = float(input("What is number 2? "))

  return (number1, number2)

operation = input("What calculation would you like to do? (add, sub, mult, div) ")

if operation == "add":
  number1, number2 = get_numbers()
  result = round(number1 + number2, 2)
  print(f"Your result is {result}")
elif operation == "sub":
  number1, number2 = get_numbers()
  result = round(number1 - number2, 2)
  print(f"Your result is {result}")
elif operation == "mult":
  number1, number2 = get_numbers()
  result = round(number1 * number2, 2)
  print(f"Your result is {result}")
elif operation == "div":
  number1, number2 = get_numbers()
  result = round(number1 / number2, 2)
  print(f"Your result is {result}")
else:
  print("That was not a valid operation!")
