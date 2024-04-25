phones={
    "john":9848,
    "ria":8989,
    "joy":9007,     
}
print(phones)
print(type(phones))
print(len(phones))

# acess items of dictionary
print(phones["john"])
print(phones.keys())
# update value in dictionary
phones["john"]= 12345
print(phones)
#add elements 
phones["kia"]=8888
print(phones)
#duplicates are not allowed
phones["john"]=988890
print(phones)

more_phones={
    "ramya":9233
}
phones.update(more_phones)
print(phones)
#Removing elemnts from dictionary
phones.pop("john")
print(phones)
print("john is removed")
print("another function canbe used that is popitem")
#pop item removes last item
phones.popitem()
print(phones)
#clear fn empties the dictionary
#phones.clear()
print(phones)

#printing the values of dictionary
for x,y in phones.items():
    print(x,y)