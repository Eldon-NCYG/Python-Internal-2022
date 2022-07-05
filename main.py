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



#Component 3: Uniform Product List --------------------------------------------------
      
#Printing the category of products depending on the user's choice
def show_products(selection):
  if selection == "male":
    for product in male_list:
      print(product["key"] + ": " + product["title"])                             
  elif selection == "female":
    for product in female_list:
      print(product["key"] + ": " + product["title"])
  elif selection == "unisex":
    for product in unisex_list:
      print(product["key"] + ": " + product["title"])


#Appending the items that the user selects into this list (global)
shopping_cart = []
      

#Error handing for user size input
def input_size():
  global size
  sizes = ["xs", "s", "m", "l", "xl"]
  size = input("Size (XS, S, M L, XL): ")
  size = size.lower().strip()

  if size not in sizes:
    print("Please input a valid size.")
    input_size()
  else:
    pass
  

#Adding product and details to shopping cart
def add_to_cart(item, category):
  product = list(filter(lambda product: product["key"] == item, category))[0]

  #Assigning the product properties/details
  name = product["product"]
  price = product["price"]
  sizeable = product["sizeable"]

  #Only ask for size if the product is sizable
  if sizeable:
    input_size()

  quantity = inputNumber("Quantity: ", "quantity")

  #Creating the product object
  add_product = {}
  add_product["name"] = name
  add_product["quantity"] = quantity
  add_product["price"] = quantity * price

  #If the product is sizeable, add a size property to the item
  if sizeable:
    print("Added " + str(quantity) + "x " + size.upper() + " " + name + " to shopping cart.")
    add_product["size"] = size.upper()
    shopping_cart.append(add_product)
  #If teh product isn't sizeable, the size property isn't added
  else:
    print("Added " + str(quantity) + "x " + name + " to shopping cart.")
    shopping_cart.append(add_product)


 
#View female products list function
def female():
  #Printing out all of the products in the female product list
  print("\n\nFemale Uniform Shop")
  show_products("female")
  keys = [d['key'] for d in female_list]

  #User inputs a product from the female product list
  select_item = input("\nEnter in nothing to go back\nAdd item to your cart: ")
  select_item = select_item.lower().strip()

  #If product inputted by user exists in the female product list, it is added to their shopping cart.
  if select_item in keys:
    add_to_cart(select_item, female_list)
    female()
  #If user inputs nothing, the program will go back and allow the user to choose another category of products to view
  elif select_item == "":
    main(username)
  else:
    print("\Error: nPlease input a valid product's key (a, b, c, etc)")
    female()
  
#View male products list function
def male():
  #Printing out all of the male products for the user to see
  print("\n\nMale Uniform Shop")
  show_products("male")
  keys = [d['key'] for d in male_list]

  #Allowing the user to input an item to their shopping cart
  select_item = input("\nEnter in nothing to go back\nAdd item to your cart to add to cart: ")
  select_item = select_item.lower().strip()

  #If item key selected by user is available in the male product list, add it to their cart
  if select_item in keys:
    add_to_cart(select_item, male_list)
    male()
  #If user inputs nothing, the program will go back and allow the user to choose another category of products to view
  elif select_item == "":
    main(username)
  #If the user enters anything that is invalid, will tell them an error has occurred and let them try again
  else:
    print("\nError: Please input a valid product's key (a, b, c, etc)")
    male()
    


#View unisex list function
def unisex():
  #Printing out all of the products in the unisex product list
  print("\nUnisex Uniform Shop\n")
  show_products("unisex")
  keys = [d['key'] for d in unisex_list]
  
  select_item = input("\nEnter in nothing to go back\nAdd item to your cart: ")
  select_item = select_item.lower().strip()

  #If product inputted by user exists in the unisex product list, it is added to their shopping cart.
  if select_item in keys:
    add_to_cart(select_item, unisex_list)
    unisex()
  #If user inputs nothing, the program will go back and allow the user to choose another category of products to view
  elif select_item == "":
    main(username)
  #If the user enters anything that is invalid, will tell them an error has occurred and let them try again
  else:
    print("\nError: Please input a valid product's key (a, b, c, etc)")
    unisex()

    




#Component 4: Checkout (showing all of the prodcuts in the  user's shopping cart)---

#Total Price of all products in shopping cart
def checkout_price():
  total_price = 0
  for product in shopping_cart:
    total_price += product["price"] 

  return total_price


#View List of all products in shopping_cart
def shopping_cart_list(products):
  print("\n\nYour Shopping Cart:")

  #For loop to print every product in the shopping cart
  for product in products:
    x = 1
    if "size" in product.values():
      print(str(products.index(product) + 1) + ". " +     str(product["quantity"]) + "x " + product["size"] + " " + product["name"] + ": $" + str(product["price"]))
    else:
      print(str(products.index(product) + 1) + ". " + str(product["quantity"]) + "x " + product["name"] + ": $" + str(product["price"]))
    x = x + 1
  

#Remove item from shopping cart function
def remove_item():
  print("\nTo remove an item, enter in the product number\nTo go back to the shopping page, enter in nothing\nTo checkout, type 'checkout'")
  option = input("\nOption: ")

  #Checking if user input a a valid product number to remove
  if option.isdigit():
    option = int(option)
    option = option - 1

    #Use try/except block to error handle if the user inputs the 
    try:
      shopping_cart[option]
      print("Removed (" + str(shopping_cart[option]["quantity"]) + "x " + shopping_cart[option]["name"] + ") from your shopping cart.")
      shopping_cart.pop(option)
      shopping_cart_list(shopping_cart)
      remove_item()
    except IndexError:
      print("Please Input a valid item number or other option.")
      remove_item()

  #Entering nothing allows user to go back a page
  elif option == "":
    main(username)
  elif option.lower().strip() == "checkout":
    shopping_cart_list(shopping_cart)
    print("\nTotal Price: $" + str(checkout_price()) + ".00\nHave a good day!")
  #When the user inputs an invalid option, the program will allow the user to input again
  else:
    print("Error: Please enter a valid option")
    remove_item()
  
#Final function that allows user to remove items from the shopping cart or fully checkout and end the program
def final():
  shopping_cart_list(shopping_cart)
  #Allowing the user to remove an item from the shopping cart or go back to the shop pages or to fully checkout
  remove_item()


  
#Main function where user chooses which (part of component 3) 
def main(username):
  print("\nWelcome to the BDSC Uniform Shop " + username + "\n")
  print("Would you like to look at Male, Female, or Unisex products? (M/F/U)?")
  print("To view shopping cart, enter in 'v'")

  #User can choose to view male, female, unisex, or checkout
  option = ""
  option = input("Option: ")
  option = option.lower().strip()

  if option == "m":
      male()
  elif option == "f":
      female()
  elif option == "u":
      unisex()
  elif option == "v":
      final()
  #Error handling
  else:
      print("\nError: Please choose either Male, Female, or Unisex Products.")
      main(username)



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





