import unittest
from password import User

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for User class behaviors
  Args:
  unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases
    '''
    self.new_user = User( "EssyMwangi","Monica/1")

  def test_init(self):
    '''
    test__init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.username,"EssyMwangi")
    self.assertEqual(self.new_user.password,"Monica/1")
  
  def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into the user list
    '''
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)
