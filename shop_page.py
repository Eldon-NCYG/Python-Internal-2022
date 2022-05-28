
from product_list import male_list, female_list, unisex_list


shopping_cart = []

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


#Adding product and details to shopping cart
def add_to_cart(item, category):
  product = list(filter(lambda product: product["key"] == item, category))[0]
  name = product["product"]
  size = input("Size (XS, S, M L, XL): ")
  quantity = int(input("Quantity: "))
  price = product["price"]
  print("Added " + str(quantity) + "x " + size + " " + name + " to shopping cart.")
  

  
  
  


def checkout():
  print("Checkout")

def female():
  print("\nFemale Uniform Shop")

  show_products("female")

  add_item = input("\nEnter in nothing to go back\nSelect item: ")

  if add_item == "":
    main()
  

def male():
  print("\n\nMale Uniform Shop")
  show_products("male")
  keys = [d['key'] for d in male_list]



  select_item = input("\nEnter in nothing to go back\nSelect item: ")
  select_item = select_item.lower().strip()

  if select_item in keys:
    add_to_cart(select_item, male_list)
    male()
  elif select_item == "":
    main()
  else:
    print("\nPlease input a product's key (a, b, c, etc)")
    male()
    



def unisex():
  print("\nUnisex Uniform Shop\n")

  show_products("unisex")

  
  add_item = input("\nEnter in nothing to go back\nSelect item: ")
  if add_item == "":
      main()
  

def main():
  print("\nWelcome to the BDSC Uniform Shop!\n")
  print("Would you like to look at Male, Female, or Unisex products? (M/F/U)?")
  print("To checkout, enter in 'C'")
  
  option = input("Option: ")
  option = option.lower().strip()

  if option == "m":
      male()
  elif option == "f":
      female()
  elif option == "u":
      unisex()
  elif option == "c":
      checkout()
  else:
      print("\nPlease choose either Male, Female, or Unisex Products.")
      main()


main()




  