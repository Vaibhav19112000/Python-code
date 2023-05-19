lst=[2,3,5,6,87,98,899,655,445,8997,7645]
a=lst[1]
b=lst[-1]
lst.insert(1,b)
lst.insert(-1,a)
del lst[0]
del lst[-1]

print(lst)
