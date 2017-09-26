class User:
    
    def __init__ (self,username,email,password):
        self.username =username
        self.email =email
        self.password =password
        self.recipe_categories =[]

        def add_recipe_category(self,recipe_category):
            if recipe_category not in self.recipe_categories:
            self.recipe_categories.append(recipe_category)
            return "recipe category is added succesfully"
        return "recipe category already exists"

