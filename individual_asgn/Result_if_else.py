# Problem: If marks is higher than 32 then pass. 
print("Welcome to Result!")
marks = int(input("Please enter your marks out of 100: "))
if marks > 90 and marks <= 100:
    print("Congratulations! You are passed with A grade")
if marks > 80 and marks < 91:
    print("Congratulations! You are passed with B grade")
if marks > 70 and marks < 81:
    print("Congratulations! You are passed with C grade")
if marks > 60 and marks < 71:
    print("Congratulations! You are passed with B grade")
if marks <= 60:
    print("You have failed!")