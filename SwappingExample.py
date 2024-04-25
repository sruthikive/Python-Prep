#Swapping elements in the list by using temporary variable
input_list=[23,65,19,90]
temp = input_list[0]
input_list[0]=input_list[2]
input_list[2]=temp
print(input_list)