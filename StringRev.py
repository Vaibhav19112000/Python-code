str1=input("Enter String: ")
s=str1.capitalize()
rev=''
j=len(str1)-1
for i in range (len(str1)):
    rev=rev+str1[j]
    j=j-1
r=rev.capitalize()
if r==s:
    print("Palindrome")
else:
    print("Not Palindrome")
