ar1 = [1,5,10,20,40,80]
ar2=[6,7,20,80,100]
ar3=[3,4,15,20,30,70,80,120]
s1=set(ar1)
s2=set(ar2)
s3=set(ar3)
print(type(s1))
print(type(s2))
print(type(s3))
s1s2 =s1.intersection(s2)
final_set = s1s2.intersection(s3)
#print(final_set)
final_set=set(final_set)
print(type(final_set))
print("Common elements")
print(final_set)