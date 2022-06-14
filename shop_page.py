
from product_list import male_list, female_list, unisex_list
from checkout import final

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

  print(shopping_cart)


 

def female():
  print("\n\nFemale Uniform Shop")
  show_products("female")
  keys = [d['key'] for d in female_list]

  select_item = input("\nEnter in nothing to go back\nSelect item: ")
  select_item = select_item.lower().strip()

  if select_item in keys:
    add_to_cart(select_item, female_list)
    female()
  elif select_item == "":
    main()
  else:
    print("\nPlease input a product's key (a, b, c, etc)")
    female()
  

def male():
  #Printing out all of the male products for the user to see
  print("\n\nMale Uniform Shop")
  show_products("male")
  keys = [d['key'] for d in male_list]

  #Allowing the user to input an item to their shopping cart
  select_item = input("\nEnter in nothing to go back\nSelect item to add to cart: ")
  select_item = select_item.lower().strip()

  #If item key selected by user is available in the male product list, add it to their cart
  if select_item in keys:
    add_to_cart(select_item, male_list)
    male()
  #Option to go back to select the shop category
  elif select_item == "":
    main()
  #If the user enters anything that is invalid, will tell them an error has occurred and let them try again
  else:
    print("\nPlease input a product's key (a, b, c, etc)")
    male()
    



def unisex():
  print("\nUnisex Uniform Shop\n")

  show_products("unisex")
  keys = [d['key'] for d in unisex_list]
  
  select_item = input("\nEnter in nothing to go back\nSelect item: ")
  select_item = select_item.lower().strip()

  if select_item in keys:
    add_to_cart(select_item, unisex_list)
    unisex()
  elif select_item == "":
    main()
  else:
    print("\nPlease input a product's key (a, b, c, etc)")
    unisex()


def main():
  print("\nWelcome to the BDSC Uniform Shop!\n")
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
      main()


main()

final(shopping_cart)