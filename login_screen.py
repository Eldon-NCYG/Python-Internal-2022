#Importing the uniform product list from external file
from product_list import male_list, female_list, unisex_list

#Global Error Handling for user input of numbers
def inputNumber(question, message):
  while True:
    try:
      userInput = int(input(question))
    except ValueError:
      if message == "age":
        print("Error: Please input a valid age.")
        continue
      elif message == "quantity":
        print("Error: Please input a valid quantity.")
        continue
    else:
       return userInput




#Component 2: Login System ------------------------------
def login(username, password):
  
  logged_in = False

  #Checking if the username & password that has been input by the user is inside the database
  file = open("accounts.txt", "r")
  for i in file:
      a,b = i.split(",")
      b = b.strip()
      if (a == username and b == password):
          logged_in = True
          break
  file.close()

  #If the username & password exists in the database, the main main function of the program starts up and the user logs in. 
  if logged_in:
      print("Successfully logged in as " + username)
      main(username)
  else:
      #Invalid username and password inputted by the user
      print("Incorrect Username or Password. Please Try Again.")
      log_or_reg(option)

      
#Component 1: Register account ---------------------------------------
def register(username, password):
  #Adding the newly registered username & password inputted by the user into the accounts databse
  file = open("accounts.txt", "a")
  file.write("\n" + username + "," + password)
  file.close()
  print("Registered " + username)

  #After registering, the main function starts up 
  main(username)

#Allowing user to login or register depending on their option
def log_or_reg(option):
  global username
  username = ""
  password = ""

  #After choosing to login, user can input existing username & password to pass into the login component
  if option == "l":
    print("\nPlease enter your username and password to log in.\nEnter nothing in the username and password to go back.")
    username = input("Username: ")
    password = input("Password: ")
      #Going back to the login screen
    if username == "" and password == "":
      start()
      exit()
    else:
      login(username, password)

  #if the user chooses to register, they can input details to pass into teh regsiter component
  elif option == "r":
    
    #Entering details to register an account
    print("\nCreate your username and password to register.\nEnter nothing in the username and password to go back.")
    username = input("Username: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    if username == "" and password == "" and confirm_password == "":
      start()
      exit()

    age = inputNumber("Enter your age: ", "age")
  

    #Checking if the user's account details meet the requirements (long enough password length, age between 13-18, etc)     
    if len(password) >= 10:
      if password == confirm_password:
        if age >= 13 and age <= 18:
          register(username, password)
        else:
          print("Sorry, this uniform shop program is only for students of BDSC (ages 13 - 18).\n\nProgram Ended")
      else:
        print("\nError: Passwords don't match up. Please Try Again.")
        log_or_reg(option)
    else:
      print("\nYour password should be 10 characters or more. Please Try Again.")
      log_or_reg(option)















#Option for user to choose to login or register an account
def start():
  global option
  print("\nWelcome to the BDSC Uniform Shop!")
  option = input("Login or Register (L / R): ")
  option = option.strip().lower()
  #Error handling
  if option != "l" and option != "r":
    print("Error: Please enter a valid input.\n")
    start()
  else:
    log_or_reg(option)

            
#Starting the whole program
start()