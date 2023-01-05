print("Python  program  to  get  a  single  string  from  two  given  strings,  separated by a space and swap the first two characters of each string")
str1=input("String1: ")
str2=input("String2: ")
x = str2[:2] + str1[2:]
y = str1[:2] + str2[2:]
print(f"string 1 is {x}")
print(f"string 2 is {y}")
str3 = " ".join([x,y])
print(str3)