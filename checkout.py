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
