# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("What calculation would you like to do? (add, sub, mult, div)")
number1 = float(input('What is number 1?'))
number2 = float(input('What is number 2?'))

if operation == "add":
  print(f"Your result is {number1 + number2}")
elif operation == "sub":
  print(f"Your result is {number1 - number2}")
elif operation == "mult":
  print(f"Your result is {number1 * number2}")
elif operation == "div":
  print(f"Your result is {number1 / number2}")
else:
  print("That was not a valid operation!")
