import unittest #Importing the unittest module
from user import User # Importing User class
from credential import Credential #Importing Credential class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    Args: 
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = User("Imma", "1234") #create user object

    def test_init(self):
        '''
        test_init test case to test if the object is instantiated properly
        '''

        self.assertEqual(self.new_user.name,"Imma")
        self.assertEqual(self.new_user.password,"1234")




class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behavious
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''