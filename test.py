shopping_cart = [{'name': 'Junior Boys Short Sleeve Shirt', 'quantity': 2, 'price': 94, 'size': 'S'}, {'name': 'Senior Boys Socks', 'quantity': 5, 'price': 9, 'size': 'S'}]


def checkout_price():
  total_price = 0
  for product in shopping_cart:
    total_price += product["price"] 

  return total_price


#Remove item from shopping cart function
def remove_item():
  option = input("Option: ")
  if option.isdigit():
    option = int(option)
    option = option - 1
    if option <= (len(shopping_cart) + 1) and option != 0:
      print("Removed (" + str(shopping_cart[option]["quantity"]) + "x " + shopping_cart[option]["name"] + ") from your shopping cart.")
      print(shopping_cart[option]["quantity"])
      shopping_cart.pop(option)
      print(shopping_cart)

    remove_item()
  elif option == "":
    main(username)
  elif option.lower().strip() == "checkout":
    print("\nTotal Price: $" + str(checkout_price()) + ".00\n Have a good day!")
  else:
    print("Please enter a valid option")
    remove_item()

remove_item()