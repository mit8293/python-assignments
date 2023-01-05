range = int(input("Please enter the range : "))
n_1 = 0
n_2 = 1
count = 0
if range < 0:
  print("Please enter the positive number! ")
elif range == 1:
  print("Your sequence : ",n_1)
elif range > 1:
  print("Your sequence :")
  while count<range:
    print(n_1)
    nth = n_1 + n_2
    n_1 = n_2
    n_2 = nth
    count += 1