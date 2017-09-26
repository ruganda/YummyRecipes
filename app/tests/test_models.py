import unittest
from app.models import User,Recipe_category,Recipe

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("ruganda", "mubaruganda@gmail.com", "password")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')
    
    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

