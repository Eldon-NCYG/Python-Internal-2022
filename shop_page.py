shopping_cart = []


def female():
    print("\nFemale Uniform Shop")
    add_item = input("ABC: ")
  
    if add_item == "":
        main()

def male():
    print("\nMale Uniform Shop")
    add_item = input("ABC: ")
    if add_item == "":
        main()

def unisex():
    print("\nUnisex Uniform Shop")
    add_item = input("ABC: ")
    if add_item == "":
        main()
    

def main():
    print("\nWelcome to the BDSC Uniform Shop!")
    option = input("Would you like to look at Male, Female, or Unisex products? (M / F / U): ")
    option = option.lower().strip()

    if option == "m":
        male()
    elif option == "f":
        female()
    elif option == "u":
        unisex()
    else:
        print("\nPlease choose either Male, Female, or Unisex Products.")
        main()


main()
    



    