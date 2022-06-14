
def final(products):
  print("\n\nYour Shopping Cart:")
  for product in products:
    x = 1
    if "size" in product.values():
      print(str(products.index(product) + 1) + ". " + str(product["quantity"]) + "x " + product["size"] + " " + product["name"] + ": $" + str(product["price"]))
    else:
      print(str(products.index(product) + 1) + ". " + str(product["quantity"]) + "x " + product["name"] + ": $" + str(product["price"]))
    x = x + 1

  print("\nTo remove an item, enter in the product number\nTo go back to the shopping page, enter in nothing")
  option = input("Option: ")

