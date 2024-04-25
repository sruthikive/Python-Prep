num = int(input("Enter a +ve number"))
#checing if the number is divisible by 15
if num % 15 == 0:
    print("NUmber is divisible by 15")
else:
#checking if divisible by 3 or 5    
    print("not divisible by 15") 
    if num % 3 ==0 or num%5==0:
        print(("Number not divisible by 15 but divisible by 3 or 5"))
    else:
        print("number is neither divisible by 3 or 5")
        print("paagal")       