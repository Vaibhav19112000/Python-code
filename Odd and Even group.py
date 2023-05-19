lst=[2,3,5,6,87,98,899,655,445,8997,7645]
lst1=[]
lst2=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
    elif i%2!=0:
        lst2.append(i)
print(lst1)
print(lst2)

#print(dir(list))
