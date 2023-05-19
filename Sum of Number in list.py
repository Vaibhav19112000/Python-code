lst=[-1,2,3,4,-4,5,8,9]
sum1=0
sum2=0
sum3=0
for i in lst:
    if i > 0:
        if i%2==0:
            sum1=sum1+i
        elif i%2!=0:
            sum2=sum2+i
    elif i<0:
        sum3=sum3+i
print("sum of Negative number : ",sum3)
print("sum of Positive Odd number : ",sum2)
print("sum of Positive Even number : ",sum1)     
