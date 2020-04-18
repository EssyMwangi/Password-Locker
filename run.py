#!/usr/bin/env python3
from password import User, Credentials

def function():
	print("               ____                                                    | |     |  |                      | | / /                                       ")
	print("              |  _ \   _____ ____  ____  ___    ___  _____  ______   __| |     |  |     _____    _____   | |/ /    ______  ______                     ")
	print("              |  __/  / _  |/ __  / __   \  \__/  / /  _  \ | |__|  / _  |     |  |    /  _  \  |  ___|  |   |    |  _ _/  | |__|                     ")
	print("              | |    / (_| |\__ \ \__ \   \  /\  /  ( (_) ) | |    / (_| |     |  |__  ( (_) )  | |___   | |\ \   | (_)__  | |                        ")
	print("              |_|    \_____| ___/  ___/    \/  \/   \_____/ |_|    \_____|     |_____| \_____/  |_____|  |_| \_\  |______| |_|                        ")

function()
  
  
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

 
def save_user(User):
    '''
    Function to save user
    '''
    User.save_user()

def create_new_credential(account_platform,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account_platform,userName,password)
    return new_credential
def save_credentials(Credentials):
    """
    Function to save Credentials to the credentials list
    """
    Credentials. save_details()

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def display_account_details():
  '''
  function that displays account deatails
  '''
  return Credentials.display_credentials()


def delete_credentials(Credentials):
  '''
  function that deletes credentials from credentials list
  '''
  Credentials.delete_credentials()

def find_credentials(account_platform):
  '''
  Function that finds existing credentials using account_platform from credentials list
  '''
  return Credentials.find_credential(account_platform) 
  

def check_credentials(account_platform):
  '''
  Function that checks if a credential exists in credentials list
  '''
  return Credentials.credential_exist(account_platform)

# def generate_Password(self):
#   '''
#   generates a random password.
#   '''
#   gen_password = generate_Password(self)
#   return gen_password

def copy_username(account_platform):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_username(account_platform)  

def main():
    print("Hello Welcome to your Password Locker...\n Please enter one of the following to proceed.\n C ---  Create New Account  \n Y ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "c":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" T - To type your own pasword:\n G - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 't':
                password = input("Enter Password\n")
                break
            # elif password_Choice == 'g':
            #     password = generate_Password()
            #     break
            else:
                print("Invalid password please try again")
        save_user(create_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "y":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker ")  
            print('\n')
    while True:
        print("Use these short codes:\n C - Create a new credential \n DC - Display Credentials \n F - Find a credential \n G - Generate A randomn password \n D - Delete credential \n E - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "c":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account_platform = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" T - To type your own pasword if you already have an account:\n G - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 't':
                    password = input("Enter Your Own Password\n")
                    break
                # elif password_Choice == 'g':
                #     password = generate_Password()
                #     break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account_platform,userName,password))
            print('\n')
            print(f"Account Credential for: {account_platform} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_account_details():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account_platform in display_account_details():
                    print(f" Account_platform:{account_platform.account_platform} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "f":
            print("Enter the Account Name you want to search for")
            account_platform = input().lower()
            if find_credentials(account_platform):
                search_credential = find_credentials(account_platform)
                print(f"Account Platform : {search_credential.account_platform}")
                print('-' * 50)
                print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            account_platform = input().lower()
            if find_credentials(account_platform):
                search_credential = find_credentials(account_platform)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account_platform} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        # elif short_code == 'g':
        #     password = generate_Password()
        #     print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'e':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    main()