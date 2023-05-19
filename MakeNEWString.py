str1=input("Enter string: ")
str2=""
if len(str1)>2:
    for i in range(2):
        str2=str2+str1[i]
    for j in range (-2,0,1):
        str2=str2+str1[j]
else:
    print("pls enter at least 3 charachter")
print(str2)     
