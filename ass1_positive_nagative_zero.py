#Dynamically see if the number is positive , nagative or zero
print("Welcome to the testing program to see your number is positive , nagative or zero")
number = int(input("Please enter a number: "))
if number > 0:
    print("The number is Positive")
elif number == 0:
    print("The number is Zero")
elif number < 0:
    print("The number is Nagative")
else:
    print("Invalid Input")