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
