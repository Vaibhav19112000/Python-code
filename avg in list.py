lst=[1,2,3,4,5,6,7]
print(type(lst))
sum=0
avg=0
for i in lst:
    sum=sum+i
    avg=sum//len(lst)
print (avg)
