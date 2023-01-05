print("program to calculate sum of 3 integars if 2 int are same sum will be zero")
x = int(input("Please enter value of x: "))
y = int(input("Please enter value of y: "))
z = int(input("Please enter value of z: "))
sum = x + y + z
if x == y:
  sum = 0
  print(f"Sum is {sum}")
elif y == z:
  sum = 0
  print(f"Sum is {sum}")
elif x == z:
  sum = 0
  print(f"Sum is {sum}")
else:
  print(f"Sum is {sum}")


print("program that will return true if the two given integers are equal or their sum or their diff is 5")
a = int(input("Please enter value of a: "))
b = int(input("Please enter value of b: "))
ret = False
if a == b or a + b == 5 or a - b == 5:
  ret = True
  print(ret)
else:
  print(ret)

print("Program for sum of n positive integars")
n = int(input("Please enter the number to get the total sum of positive int: "))
start = 1
total_sum = (n * (n + 1))/2
print(int(total_sum))