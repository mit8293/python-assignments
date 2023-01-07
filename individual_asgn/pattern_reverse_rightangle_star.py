rows = 5
for i in range(1,6):
    for j in range(1,6):
        if (j <= rows - i):
            print(" ", end = " ")
        else:
            print("*", end = " ")
    print()

for k in range(1,6):
    print(" " * (rows - k) +"*" * k)