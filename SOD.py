no=int(input("enter number : "))
no1=no
count=0
sum=0
while no > 0:
    no=no//10
    count += 1
for i in range (count):
    n=no1%10
    no1=no1//10
    sum=sum+n
print(sum) 
