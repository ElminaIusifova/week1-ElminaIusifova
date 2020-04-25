# # Divide the apples
# ![](apple2.gif)
#
#
# n schoolchildren divide k apples evenly, the residue remains in the basket. How many apples will get each child?
#
# ### Input
# Two positive integers n and k, not greater than 1500 - rarely happens in school more pupils, and too many apples to eat bad ...
#
# ### Output
# Print the number of apples that goes to each child.
n =int(input("Enter the number of schoolchildren "))
k =int(input("Enter the number of apples "))


if (n < 1500) and (k < 1500):
    t=k//n
    print("Each child will have ", t,"apples")
else:
    print("Wrong number, entered value has to be not more than 1500")
