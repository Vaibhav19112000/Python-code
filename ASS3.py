s1=int(input("Enter Marks  : "))
s2=int(input("Enter Marks  :"))
s3=int(input("Enter Marks  :"))
s4=int(input("Enter Marks  :"))
s5=int(input("Enter Marks  :"))
sum=s1+s2+s3+s4+s5
percent=((sum*100)/500)
if (percent>=75):
	print("Distinction")
elif (percent>=60 and percent<=75):
	print("First Class")
elif (percent>=35 and percent<60):
	print("Second Class")
else:
	print("Study Hard")