def main():
    # print("Logged in")
  pass


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
        main()
    else:
        print("Incorrect Username or Password.")
        log_or_reg(option)

def register(username, password):
    file = open("accounts.txt", "a")
    file.write("\n" + username + "," + password)
    file.close()
    print("Registered " + username)
    main()


def log_or_reg(option):
    username = ""
    password = ""
  
    if option == "l":
        print("\nPlease enter your username and password to log in.\nEnter nothing in the username and password to go back.")
        username = input("Username: ")
        password = input("Password: ")
        if username == "" and password == "":
            start()
            exit()
        else:
            login(username, password)
    else:
        print("\nCreate your username and password to register.\nEnter nothing in the username and password to go back.")
        username = input("Username: ")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")
        if username == "" and password == "" and confirm_password == "":
            start()
            exit()
      
        if len(password) >= 10:
            if password == confirm_password:
                register(username, password)
            else:
                print("\nError: Passwords don't match up. Please Try Again.")
                log_or_reg(option)
        else:
            print("\nYour password should be 10 characters or more. Please Try Again.")
            log_or_reg(option)



def start():
    global option
    print("\nWelcome to the BDSC Uniform Shop!")
    option = input("Login or Register (L / R): ")
    option = option.strip().lower()
    log_or_reg(option)
    if option != "l" and option != "r":
        print("Please enter a valid input.\n")
        start()
            

start()
log_or_reg(option)
