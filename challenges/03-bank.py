balance = 4000
print("Welcome to Chase bank.")

def deposit():
  return float(input("How much would you like to deposit?\n"))

def withdraw():
  return float(input("How much would you like to withdraw?\n"))

def print_balance():
  print(f"Your current balance is:\n{balance}")

print_balance()
is_done = "no"

# main loop
while is_done != "yes":
  command = input("\nWhat would you like to do? (deposit, withdraw, balance)\n")
  if command == "deposit":
    balance += deposit()
  elif command == "withdraw":
    balance -= withdraw()

  print_balance()
  is_done = input("Are you done?\n")

print("Have a nice day!")
