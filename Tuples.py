#creating a tuple
colours = ("red","yellow","green")
#creating a tuple with one item
vegetable = ("carrot")
fruit=("apple"), # , used so that it is recognised as a tuple as there is only one item
#check type of  tuple
print(type(fruit))
print(type(vegetable)) #considered a string cause tehre is no ,
#check length of tuple
print(len(colours))
#accessing the items in tuple
# +ve indexing Left to Right
print(colours[1])
print(colours[0])
print(fruit[0])
# -ve indexing
print(colours[-1])
#range indexing +ve
print(colours[1:3]) 
#range indexing -ve
print(colours[-2:0])

#check if an item exists or not
if "green" in colours:
    print("green is a part of colours")

#traverse a tuple
for i in colours:
    print(i)

# concatenate  2 tuples
#more_colours = ("blue","brown")
#colours = colours+more_colours
#print(more_colours)
#unpacking a tuple
print("unpacking a tuple")
colour1, colour2,colour3 = colours
print(colour1,colour2,colour3)