import unittest
from app.models import User,Recipe_category,Recipe

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("ruganda", "mubaruganda@gmail.com", "password")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')
    
    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')
    
    def test_add_recipe_category_category_added(self):
        self.assertEqual(self.user.add_recipe_category("dinner"),
                        "recipe category is added succesfully")
    
    def test_add_recipe_category_name_already_exists(self):
        self.user.add_recipe_category("dinner")
        self.assertEqual(self.user.add_recipe_category
                         ("dinner"),
                         "recipe category already exists")
    def test_edit_recipe_category_not_found(self):
        self.assertEqual(self.user.edit_recipe_category("absent", "newtype"),
                         "recipe_category not found")
    def test_edit_recipe_category_successful(self):
        self.user.add_recipe_category("Snacks")
        self.assertEqual(self.user.edit_recipe_category("Snacks","local foods"),"recipe_category not found")

    def test_delete_recipe_category_not_found(self):
        self.assertEqual(self.user.delete_recipe_category("not exist"), "recipe_category not found")
    
    def test_delete_recipe_category_deleted(self):
        self.user.add_recipe_category("lunch recipes")
        self.assertEqual(self.user.delete_recipe_category("lunch recipes"),
                         "recipe_category deleted")
    
    



