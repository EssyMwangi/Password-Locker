import unittest
import pyperclip
from password import User
from password import Credentials


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
        self.new_user = User("EssyMwangi", "Monica/1")

    def test_init(self):
        '''
        test__init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username, "EssyMwangi")
        self.assertEqual(self.new_user.password, "Monica/1")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for Credentials class behaviors
    Args:
      unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set Up method to run before each test case"
        '''
        self.new_credential = Credentials(
            "Instagram", "EssyMwangi", "Sonnie/1")

    def test__init(self):
        '''
        test__init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_platform, "Instagram")
        self.assertEqual(self.new_credential.username, "EssyMwangi")
        self.assertEqual(self.new_credential.password, "Sonnie/1")

    def test_save_credential(self):
        '''
        test save credentials to test if the credential object is saved into credentials list
        '''
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        teaddown method that does clean up after eachtest case has run
        '''
        Credentials.credentials_list = []

    def test_save_multiple_accounts(self):
        '''
        test checks if we can save multiple credential objects to our contact list
        '''
        self.new_credential.save_details()
        test_credentials = Credentials("Gmail", "AshleyMwangi", "Wanjiru/1")
        test_credentials.save_details()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        to test if we can remove a credential from our credentials list
        '''
        self.new_credential.save_details()
        test_credentials = Credentials("Gmail", "AshleyMwangi", "Wanjiru/1")
        test_credentials.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credential(self):
        '''
        test to check if we can find a credential by account platform and display information
        '''
        self.new_credential.save_details()
        test_credentials = Credentials("Gmail", "AshleyMwangi", "Wanjiru/1")
        test_credentials.save_details()

        found_credential = Credentials.find_credential("Gmail")

        self.assertEqual(found_credential.account_platform,
                         test_credentials.account_platform)

    def test_credential_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the contact
        '''

        self.new_credential.save_details()
        test_credentials = Credentials("Gmail", "AshleyMwangi", "Wanjiru/1")
        test_credentials.save_details()

        credential_exists = Credentials.credential_exist("Gmail")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)

    def test_copy_username(self):
        '''
        Test to confirm that we are copying the username from a found credential
        '''
        self.new_credential.save_details()
        Credentials.copy_username("Instagram")
        self.assertEqual(self.new_credential.username, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
