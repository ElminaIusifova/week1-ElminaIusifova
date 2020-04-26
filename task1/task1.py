# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs

a = int(input("Please input your first number "))
b = int(input("Please input your second number "))
c = input("Which action do you want to do with those numbers? ")
answer=0

if c == "+":
    answer=a+b
if c== "-":
    answer=a-b
if c== "*":
    answer=a*b
if c=="/":
    answer=a/b

print("Your result is: ", answer)