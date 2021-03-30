# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1


user_input = input("What string do you want to reverse? ")

def reverse(s):
  result = ''
  for char in s:
    result = char + result

  return result

print(f"{user_input} reversed is: {reverse(user_input)}")