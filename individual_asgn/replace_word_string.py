str4 = input("Enter your input:")
# if str4.find("poor") < str4.find("not"):
for i in(("not","good"),("poor","good")):
    str4 = str4.replace(*i)
print(str4)