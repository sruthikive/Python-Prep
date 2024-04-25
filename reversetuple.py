# Reversing elements in the tuple
# reversed() function is used - used to iterate through a sequence in reversed order
ALp = (1,2,3,4,5)
list= []
#add reversed values ina a list
for x in reversed(ALp):
    list.append(x)
nuew_tuple = tuple(list)     
print(nuew_tuple)