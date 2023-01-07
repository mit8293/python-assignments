num = int(input("Please enter any number: "))
flag = False
# sum = 0
# for digit in str(num):
#     sum = sum + int(digit)
#     print(sum)
if num>1:
    for i in range(2,num):
        if (num%i) == 0 :
            flag = True
            break
if flag:
    print("Not prime")
elif num == 1:
    print("Not Prime")
else:
    print("prime")