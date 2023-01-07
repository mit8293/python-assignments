
print("Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. ")
str4 = input("Enter your input:")
a = str4.find('not')
b = str4.find('poor')
if a > b:
    replace = "good"
    new_str = str4.replace("poor",replace)
    res = new_str[:new_str.index(replace) + len(replace)]
    res1 = new_str[new_str.index("not")+3:]
    print(str(res))
    print(str(res1))
    print(str(res)+str(res1))


# a = str4.split(" ")
# if a.index("not") > a.index("poor"):
#     for i in range(a.index("poor"),a.index("not")+1):
#         a[i] = "good"
#         break
#     b=' '.join(a)
#     print(a)
#     print(b)
    


# if str4.find("poor") < str4.find("not"):
# for i in(("not","good"),("poor","good")):
#     str4 = str4.replace(*i)
# print(str4)

    # b = str4.split(" ")
    # for i in range(len(b)):
    #     b[i]="good"
    #     print(b)


# string = input("Enter a string:")
# a = string.find('not')
# b = string.find('poor')
# print("Appearence of 'not':",a)
# print("Appearence of 'poor':",b)
# if a > b:
#     new_string = string
# # if b + 4 == a:
# #     print(string[0:b]+"good"+string[a+3:])
