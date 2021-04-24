print("Welcome to the calculator")
q = input('claculator or quit')
while q != 'q','quit'
   fir = int(input("Type your first number"))
   sec = int(input("Type your second number"))
   x = input("Type any operation name").lower()
   if x == "addition":
      print("The answer is " + str(fir + sec))
   elif x == "subtraction":
      print("The answer is " + str(fir - sec))
   elif x == "multiplication":
      print("The answer is " + str(fir * sec))
   elif x == "division":
      print("The answer is " + str(fir / sec))
   else:
       print("check your spelling")
print("Thank you")
