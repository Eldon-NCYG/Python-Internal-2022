#Importing the uniform product list from external file
from product_list import male_list, female_list, unisex_list
from checkout import final

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
       


#Login compoennt
def login(username, password):

  logged_in = False

  file = open("accounts.txt", "r")
  for i in file:
      a,b = i.split(",")
      b = b.strip()
      if (a == username and b == password):
          logged_in = True
          break
  file.close()

  if logged_in:
      print("Successfully logged in as " + username)
      main(username)
  else:
      print("Incorrect Username or Password. Please Try Again.")
      log_or_reg(option)

      
#Register account component
def register(username, password):
  file = open("accounts.txt", "a")
  file.write("\n" + username + "," + password)
  file.close()
  print("Registered " + username)
  main(username)


def log_or_reg(option):
  global username
  username = ""
  password = ""

  #Entering account details for Login Component
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
  elif option == "r":
    #Register account component
    print("\nCreate your username and password to register.\nEnter nothing in the username and password to go back.")
    username = input("Username: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    if username == "" and password == "" and confirm_password == "":
      start()
      exit()

    age = inputNumber("Enter your age: ", "age")
  

            
  if len(password) >= 10:
    if password == confirm_password:
      if age >= 13 and age <= 18:
        register(username, password)
      else:
        print("Sorry, this uniform shop program is only for students of BDSC")
        log_or_reg(option)
    else:
      print("\nError: Passwords don't match up. Please Try Again.")
      log_or_reg(option)
  else:
    print("\nYour password should be 10 characters or more. Please Try Again.")
    log_or_reg(option)



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
      

#Adding product and details to shopping cart
def add_to_cart(item, category):
  product = list(filter(lambda product: product["key"] == item, category))[0]

  #Assigning the product properties/details
  name = product["product"]
  price = product["price"]
  sizeable = product["sizeable"]


  #Only ask for size if the product is sizable
  if sizeable:
    size = input("Size (XS, S, M L, XL): ")

  quantity = int(input("Quantity: "))

  #Creating the product object
  add_product = {}
  add_product["name"] = name
  add_product["quantity"] = quantity

  add_product["price"] = quantity * price
  
  
  
  if sizeable:
    print("Added " + str(quantity) + "x " + size.upper() + " " + name + " to shopping cart.")
    add_product["size"] = size.upper()
    shopping_cart.append(add_product)

  else:
    print("Added " + str(quantity) + "x " + name + " to shopping cart.")
    shopping_cart.append(add_product)


 

def female():
  print("\n\nFemale Uniform Shop")
  show_products("female")
  keys = [d['key'] for d in female_list]

  select_item = input("\nEnter in nothing to go back\nAdd item to your cart: ")
  select_item = select_item.lower().strip()

  if select_item in keys:
    add_to_cart(select_item, female_list)
    female()
  elif select_item == "":
    main(username)
  else:
    print("\nPlease input a product's key (a, b, c, etc)")
    female()
  

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
  #Option to go back to select the shop category
  elif select_item == "":
    main(username)
  #If the user enters anything that is invalid, will tell them an error has occurred and let them try again
  else:
    print("\nPlease input a product's key (a, b, c, etc)")
    male()
    



def unisex():
  print("\nUnisex Uniform Shop\n")

  show_products("unisex")
  keys = [d['key'] for d in unisex_list]
  
  select_item = input("\nEnter in nothing to go back\nAdd item to your cart: ")
  select_item = select_item.lower().strip()

  if select_item in keys:
    add_to_cart(select_item, unisex_list)
    unisex()
  elif select_item == "":
    main(username)
  else:
    print("\nPlease input a product's key (a, b, c, etc)")
    unisex()


def main(username):
  print("\nWelcome to the BDSC Uniform Shop " + username + "\n")
  print("Would you like to look at Male, Female, or Unisex products? (M/F/U)?")
  print("To checkout, enter in 'C'")
  option = ""
  option = input("Option: ")
  option = option.lower().strip()

  if option == "m":
      male()
  elif option == "f":
      female()
  elif option == "u":
      unisex()
  elif option == "c":
      pass
  else:
      print("\nPlease choose either Male, Female, or Unisex Products.")
      main(username)



#Option for user to choose to login or register an account
def start():
    global option
    print("\nWelcome to the BDSC Uniform Shop!")
    option = input("Login or Register (L / R): ")
    option = option.strip().lower()
    if option != "l" and option != "r":
        print("Please enter a valid input.\n")
        start()
    else:
      log_or_reg(option)

            

start()

#Component 4: Checkout (showing all of the prodcuts in the  user's shopping cart)
def final(products):
  print("\n\nYour Shopping Cart:")

  #For loop to print every product in the shopping cart
  for product in products:
    x = 1
    if "size" in product.values():
      print(str(products.index(product) + 1) + ". " + str(product["quantity"]) + "x " + product["size"] + " " + product["name"] + ": $" + str(product["price"]))
    else:
      print(str(products.index(product) + 1) + ". " + str(product["quantity"]) + "x " + product["name"] + ": $" + str(product["price"]))
    x = x + 1

    #Allowing the user to remove an item from the shopping cart or go back to the shop pages or to fully checkout
  print("\nTo remove an item, enter in the product number\nTo go back to the shopping page, enter in nothing")
  option = input("Option: ")



final(shopping_cart)


