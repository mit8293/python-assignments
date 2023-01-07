str1 = input("Please enter the string: ")
x = str1[:2]
y = str1[-2:]

if len(str1)<2:
    print("empty string")
else:
    print(x+y)