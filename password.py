import pyperclip
import random
import string


class User:
    '''
    A Class that generates new instances of a user
    '''
    user_list = []  # Empty user list

    def __init__(self, username, password):
        '''
        __init__ method helps us define propeties for our objects
        Ars:
          username: New User username.
          passors: New Use password.
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        method that saves userobjects into user_list
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)


class Credentials():
    '''
    A class that generates new instances of credentials
    '''
    credentials_list = []

    def __init__(self, account_platform, username, password):
        '''
        __init__ method helps us define propeties for our objects
        Ars:
          username: New User username.
          passors: New Use password.
        '''
        self.account_platform = account_platform
        self.username = username
        self.password = password

    def save_details(self):
        ''' 
        method that saves credential objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        method deletesa saved credential from credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account_platform):
        '''
        method that takes in account platform and returns a credential that matches that account platform
        '''
        for credential in cls.credentials_list:
            if credential.account_platform == account_platform:
                return credential

    @classmethod
    def credential_exist(cls, account_platform):
        '''
        method that checks if a credential exists from the credentials list.
        Args:
          account_platform: to serarch if it exists
        Returns:
          Boolean: True or false depending if the credential exists 
        '''
        for credential in cls.credentials_list:
            if credential.account_platform == account_platform:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        methodthat returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def copy_username(cls, account_platform):
        found_credential = Credentials.find_credential(account_platform)
        pyperclip.copy(found_credential.username)

    @classmethod
    def verify_user(cls, username, password):
        '''
        method that verifys user is in the user list or is not
        '''
        the_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                the_user == user.username
        return the_user

    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + \
            string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
