print("Python function to insert a string in the middle of a string.")

str1 = input("Enter string1 : ")
str2 = input("Enter middle string : ")
midString = len(str1)//2
str3 = str1[:midString]+str2+str1[midString:]
print(str3)