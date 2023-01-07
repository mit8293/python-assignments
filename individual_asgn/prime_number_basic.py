num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
        if (num % i) == 0:
           print("Not Prime")
           break
    else: # Executes only when loop is terminated naturally. or it will not print. Entire loop iteration will be finished then it will executed
        print("Prime")

else:
   print("Not Prime")