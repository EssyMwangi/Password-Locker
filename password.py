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


    
