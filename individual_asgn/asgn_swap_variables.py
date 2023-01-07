#program to swap variables using temp and without using temp
x = int(input("Please enter value of x : "))
y = int(input("Please enter value of y : "))
temp = x
x = y
y = temp
print(f"value of x is {x}")
print(f"value of y is {y}")

#without using temp
a = int(input("Please enter value of a : "))
b = int(input("Please enter value of b : "))
a , b = b , a
print(f"value of a is {a}")
print(f"value of b is {b}")