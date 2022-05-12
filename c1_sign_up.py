def login(username, password):
    print("Logged in", username, password)


def register(username, password):
    print("Registered", username, password)


def log_or_reg(option):
    if option == "l":
        username = input("\nUsername: ")
        password = input("Password: ")
        login(username, password)
    else:
        print("\nCreate your username and password to register.")
        username = input("Username: ")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")

        if len(password) >= 10:
            if password == confirm_password:
                register(username, password)
            else:
                print("\nError: Passwords don't match up.")
                log_or_reg(option)
        else:
            print("\nYour password should be 10 characters or more.")
            log_or_reg(option)





def start():
    global option
    print("\nWelcome to the BDSC Uniform Shop!")
    option = input("Login or Register (L / R): ")
    option = option.strip().lower()
    if option != "l" and option != "r":
        print("Please enter a valid input.\n")
        start()


start()
log_or_reg(option)
