#To check any given number is in table of 1 to 10. 
# example number 20
# output: 
# it is in 2 table
# it is in 4 table
# it is in 5 table
# it is in 10 table

print("Check your number is in which table number between 1 to 10")
number = int(input("Please enter the number"))
if number % 1 == 0 and number >= 1 and number <= 10:
    print("It is in table of 1")
if number % 2 == 0 and number <= 2 and number <= 20:
    print("It is in table of 2")
if number % 3 == 0 and number <= 3 and number <= 30:
    print("It is in table of 3")
if number % 4 == 0 and number <=40:
    print("It is in table of 4")
if number % 5 == 0 and number <=50:
    print("It is in table of 5")
if number % 6 == 0 and number <=60:
    print("It is in table of 6")
if number % 7 == 0 and number <=70:
    print("It is in table of 7")
if number % 8 == 0 and number <=80:
    print("It is in table of 8")
if number % 9 == 0 and number <=90:
    print("It is in table of 9")
if number % 10 == 0 and number <=100:
    print("It is in table of 10")
# if ((number % 1 == 0 and number <= 10 and number => 1)) and (number % 2 == 0 and number >= 2 and number <= 20) and (number % 3 == 0 and number >= 3 and number <= 30) and (number % 4 == 0 and number <=40 and number >= 4) and (number % 5 == 0 and number >=5 and number <=50) and (number % 6 == 0 and number <=60 and number >=6) and (number % 7 == 0 and number >=7 and number <=70) and (number % 8 == 0 and number <=80 and number <=8) and (number % 9 == 0 and number >=9 and number <=90) and (number % 10 == 0 and number <=100 and number>=10)):
#     print("Invalid input")