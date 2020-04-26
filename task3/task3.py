# # Even or Odd
# Positive integer n is given. Determine its parity.
# ## Input
# One positive integer n;
# ## Output
# If number n is even, print `EVEN`. If number is odd, print `ODD`.

num = int(input("Please enter your number: "))
if num % 2 == 0:
    print("Your number is EVEN")
if num % 2 == 1:
    print("Your number is ODD")