lst=[1,2,7,6,5,53,4,5,6,8,9,9,9,7,4,3]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
        print(f"{i} :",lst.count(i))


        
 
