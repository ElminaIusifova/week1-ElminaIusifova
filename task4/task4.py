# # City numbers
# Determine if the houses with numbers n and m are located on one side of the street.
# ## Input
# Two numbers n and m (1 ≤ n, m ≤ 100).
# ## Output
# Print 1 if the houses with numbers n and m are located on one side of the street and 0 otherwise.
#
n = int(input("Please enter first number: "))
m = int(input("Please enter second number: "))

if 1 <= n <= 100 and 100 >= m >= 1:
    if n % 2 == 0 and m % 2 == 0:
        print("1")
    # if n % 2 == 1 or m % 2 == 1:
    else:
        print("0")
else:
    print("Invalid number")





#
#
#
#
#
#
#
#
