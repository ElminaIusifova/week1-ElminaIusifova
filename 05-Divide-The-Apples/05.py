# # Divide the apples
# ![](apple.jpg)
#
#
# n schoolchildren divide k apples evenly, the residue remains in the basket. How many apples remains in the basket?
#
# ### Input
# Two integers n and k not greater than 1500 - rarely happens in school more pupils, and where to find such a basket?
#
# ### Output
# Print the number of apples in the basket.
n =int(input("Enter the number of schoolchildren"))
k =int(input("Enter the number of apples"))
if (n < 1500) and (k < 1500):
    t=k%n
    print("There are", t,"apples left in the basket")
else:
    print("Wrong number, entered value has to be not more than 1500")
