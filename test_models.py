import unittest
from models import User,Recipe_category,Recipe

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("ruganda", "mubaruganda@gmail.com", "password")

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
        
    def test_view_recipe_category(self):
        self.assertEqual(self.user.view_recipe_category(" "), "recipe_categories is empty")

class Recipe_categoryTest(unittest.TestCase):
    
    def setUp(self):
        self.recipes = Recipe_category("")

    def test_recipe_instantiation(self):
        self.assertIsInstance(self.recipes, Recipe_category,
                              "Failed to instantiate")

    def test_add_recipe_added(self):
            self.assertEqual(self.recipes.add_recipe("pillawo"), "recipe added succesfully")

    def test_add_recipe_exists(self):
        self.recipes.add_recipe("pizza")
        self.assertEqual(self.recipes.add_recipe(
            "pizza"), "recipe already exists")

    def test_edit_recipe_not_found(self):
        self.assertEqual(self.recipes.edit_recipe(
            "chicken recipe", "beef recipe"), "no recipe to edit")

   
    def test_edit_recipe_edited_succesfully(self):
         self.recipes.add_recipe("pizza")
         self.assertEqual(self.recipes.edit_recipe("chicken", "pizza"), "recipe added successfully")

    def test_delete_recipe_not_found(self):
          self.assertEqual(self.recipes.delete_recipe(
            "katogo"), "No recipe to delete")

    def test_recipe_item(self):
        self.recipes.add_recipe("katogo")
        self.assertEqual(self.recipes.delete_recipe("katogo"), "recipe deleted")

    def test_view_recipe(self):
        self.assertEqual(self.recipes.view_recipe(" "), "no recipe found")
