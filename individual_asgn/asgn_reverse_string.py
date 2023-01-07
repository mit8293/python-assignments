print(" Python function to reverses a string if its length is a multiple of 4. ")
str1 = input("Please enter string : ")
str2 = ''
if len(str1) % 4 == 0:
    for i in str1:
        str2 = i + str2
    print(str2)
