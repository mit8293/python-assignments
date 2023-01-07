print("Python  function  that takes a list of words and returns the length of the longest one. ")
list1 = input("Please enter the words with space for your list : ").split()
print(list1)
count = -1
for i in list1:
    if len(i) > count:
        count = len(i)
        result = i
print(f"Biggest word is : {result}")
print(f"Length is : {count}")