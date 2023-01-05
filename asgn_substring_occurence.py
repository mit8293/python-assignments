print("Program to count occurrences of a substring in a string.")
str1 = input("Please enter input : ")
str2 = input("Please enter substring : ")
count = 0
for i in range(len(str1)-len(str2)+1):
    if(str1.startswith(str2,i)):
        count+=1
print(count)


print("program to count the occurrences of each word in a given sentence")
str3 = input("Please enter a string : ")
a=str3.split(" ")
count1=0
for j in range(len(a)):
    if a[j].isalpha():
        count1+=1
print(count1)