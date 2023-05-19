lst=[2,3,5,5,6,7,8,899,6,2,87,98,899,655,445,8997,7645]

for i in range (len(lst)):
    if i in lst:
        del lst[i]
print(lst)

print(dir(list))
