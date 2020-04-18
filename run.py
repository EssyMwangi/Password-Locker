#!/usr/bin/env python3
from password import User, Credentials

# def function():
# 	print("               ____                                                    | |     |  |                      | | / /                                       ")
# 	print("              |  _ \   _____ ____  ____  ___    ___  _____  ______   __| |     |  |     _____    _____   | |/ /     ______  ______                     ")
# 	print("              |  __/  / _  |/ __  / __   \  \__/  / /  _  \ | |__|  / _  |     |  |    /  _  \  |  ___|  |    |    |  _ _/  | |__|                     ")
# 	print("              | |    / (_| |\__ \ \__ \   \  /\  /  ( (_) ) | |    / (_| |     |  |__  ( (_) )  | |___   |  |\ \   | (_)__  | |                        ")
# 	print("              |_|    \_____| ___/  ___/    \/  \/   \_____/ |_|    \_____|     |_____| \_____/  |_____|  |__| \_\  |______| |_|                        ")

# function()

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

