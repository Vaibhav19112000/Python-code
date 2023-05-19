str1="NumberisTen"
s=str1.lower()
count=0
vowel="aeiou"
for i in range(len(str1)):
    if str1[i] not in vowel:
        count=count+1
print(count)
