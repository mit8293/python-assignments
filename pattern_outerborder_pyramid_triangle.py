####*
###*#*
##*###*
#*#####*

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end = "")
    for j in range(i+1):
        if j == 0:
            print("*",end = "")
        else:
            print(" ",end = "")
    for j in range(i):
        if j == i-1:
            print("*",end = "")
        else:
            print(" ",end = "")
    print()