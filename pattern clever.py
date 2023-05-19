str1=input("enter string : ")

for i in range (len(str1)):
    j=0
    while j<=i:
        print(str1[j],end="")
        j=j+1
    print()
