no=int(input("enter number : "))
no2=no
count=0
rev=""
while no > 0:
    no=no//10
    count += 1
for i in range (count):
    n=no2%10
    no2=no2//10
    rev=rev+str(n)
print(rev) 



