#programm to check letter is vowel or not
x = input("Please enter a letter : ").lower()
if len(x) == 1 and x.isalpha():
  if x in ('a','e','i','o','u'):
    print("letter is vowel")
  else:
    print("Letter is not vowel")
else:
  print("Please enter only 1 alphabet")