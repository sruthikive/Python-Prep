#list comprehensionfruits = ["apple","mango","cherry"]
fruits = ["apple","mango","cherry"]
new_fruits = [fruits for fruits in fruits if "a" in fruits ]
print(new_fruits)

#copy a list
new_fruits=fruits.copy()
print(new_fruits)

new_fruit = fruits+new_fruits
print(new_fruit)
print("_____NESTED LISTS____")
#NESTED LIST
fruits.insert(2,["kiwi","papaya"])
print(fruits)
print(fruits[2])
print(fruits[2][0])