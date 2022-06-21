#How to make sure the user enters a number (integer) - www.101computing.net

def inputNumber(message):
  while True:
    try:
      userInput = int(input(message))
      break
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 
     

#MAIN PROGRAM STARTS HERE:
age = inputNumber("How old are you?")

if (age>=18):
  print("You are old enough to vote.")
else:
  print("You will be able to vote in " + str(18-age) + " year(s).")

     