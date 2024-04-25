# Mirror the characters from the nth position upto the length of the string in
# ZIP function is used
input_string = input("Enter string:")
n=int(input("enter n: "))
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alp = alphabets[::-1]
print(reverse_alp)
dict1=dict(zip(alphabets,reverse_alp))
# finding the part of string on which we willl do mirror operaton
prefix=input_string[0:n-1]
suffix=input_string[n-1:]
#finding the mirror string 
mirror = ""
for i in range(0,len(suffix)):
    mirror=mirror+dict1[suffix[i]]

#creating the final string
result = prefix+mirror
print(result)    