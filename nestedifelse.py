#find the greatest of the taken three numbers
n1 = int(input("enter a number: "))
n2 = int(input("enter a number: "))
n3 = int(input("enter a number: "))
#using nested if else statement
if n1>n2:
    #either n1 or n3 is greatest
    if n1>n3:
        print("n1 is greatest")
    else:
        print("n3 is greatest")
else:
    #either n2 or n3 is greatest
    if n2>n3:
        print("n2 is greatetst")
    else:
        print("print n3 is greatest")    


