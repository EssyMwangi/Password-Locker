class User:
  '''
  A Class that generates new instances of a user
  '''
  user_list = [] #Empty user list

  def __init__(self,username,password):
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



class Credentials():
  '''
  A class that generates new instances of credentials
  '''
  credentials_list = []

  def __init__(self,account_platform,username,password):
    '''
    __init__ method helps us define propeties for our objects
    Ars:
      username: New User username.
      passors: New Use password.
    '''
    self.account_platform = account_platform
    self.username = username
    self.password = password
 