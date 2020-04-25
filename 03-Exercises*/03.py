# # Exercises
# 1. Write a Python program to parse a string to Float or Integer.

int1 = int("13")
int2 = int(3.2)
print("Task 1")
print(int1, int2)



# 2. Given variables x=30 and y=20, write a Python program to print t "30+20=50".

x=30
y=20
t=x+y
print ("Task 2")
print("t=",t)

# 3. Enter the value with the input. Convert the entered value to integer. Print the value obtained by dividing that value by 2, 3, 5, and 10.
print("Task 3")
value1 = int(input("Enter a number:"))
value2 = value1//2
value3 = value1//3
value4 = value1//5
value5 = value1//10
values =[value2, value3, value4, value5]
print("Your final result is ", values)


# 4. Enter the value with the input. Convert the entered value to integer. Print the remainder of the value divided by 2, 3, 5, and 10.

print("Task 4")
value1 = int(input("Enter a number:"))
value2 = value1%2
value3 = value1%3
value4 = value1%5
value5 = value1%10
values =[value2, value3, value4, value5]
print("Your final result is ", values)

