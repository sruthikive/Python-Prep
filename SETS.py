#unordered
#immutable
#unidexed
#duplicates not allwowed
#CREATING A SET
names={"sia","Mia","Tia"}
print(names) #unordered
print(len(names)) #six=ze of set
print(type(names)) #typecasting
for x in names:
    print(x)
#check if item exists in set
if "sia" in names:
    print("Sia is in names")
else:
    print("not there")
# adding elements to set
names.add("Sita")
print(names) 
print("trying to add same/duplicate") 
#no result
names.add("sia") 
print(names)
 #add another sequence in a set
print("UPDATING")
names_list = ["ria","kia"]
names.update(names_list)
print(names)

#for removing elements
print("Removing elements")
#names.remove("ria")
names.discard("ria")#discard wont throw a error like remove function if there is no element given
print(names)

#joining sets
print("UNion of sets function")
s1 ={1,2,3}
s2={3,2,6}
#s3 = s1.union(s2)
#print(s3)
#OR
# updating sets
#s1.update(s2)
#print(s1)

#keep only duplicates while joining
#keeps only common elements in both set
print("Intersction update")
s1.intersection_update(s2)
print(s1)
#keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)
