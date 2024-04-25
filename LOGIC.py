exp1 = 2>3
exp2 = 3>2
print(exp1 and exp2)
print(exp1 or exp2)
print(not(exp1))

#identity operators
x = 5
y = 5
print(x is y)
print(x is not y)

#membership operators
fruits = ["banana","apple","pear"]
print("pear" in fruits)
print("pear" not in fruits)
print("mango"in fruits)
print("mango"not in fruits)
#bitwisde operators
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b )