print("Python  program to add 'ing'  at the end of a given  string  (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if  the  string  length  of  the  given  string  is  less  than  3,  leave  it unchanged")
str1 = input("Please enter a string: ")

if str1.endswith("ing"):
    str2 = 'ly'.join(str1.rsplit("ing",1))
    print(str2)
elif len(str1) > 3:
    print(f"{str1}ing")
else:
    print(str1)