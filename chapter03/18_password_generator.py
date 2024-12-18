import random, string

# list of characters
characters = list(string.ascii_letters + string.digits + " !@#$%^&*")

def generate_password():
    """
    Generates a random password based on the user-specific length.
    """    
    try:
        password_length = int (input("Give the password length: "))
        
        if password_length <= 0:
            print("Password length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please give a valid number")
        return
    
    random.shuffle(characters)
    
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "".join(password)
    
    print(f"\nGenerated Password: {password}")

def main():
    # my_list = list("Jim")
    # print(my_list)
    while True:
        option = input("\nDo you want to create a password? ('y' for yes or 'q' for quit): ")
        
        if option.lower() == 'y':
            generate_password()
        elif option.lower() == 'q':
            print("Goodbye")
            break
        else:
            print("Wrong input")

if __name__ == "__main__":
    main()