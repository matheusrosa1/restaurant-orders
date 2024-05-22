       self.sorce_path = source_path
        self.dishes = set()
        self.ingredients = set()
        self.load_data()

    def load_data(self):
        with open(self.sorce_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                dish = Dish(row["dish"], row["price"])
                ingredient = Ingredient(row["ingredient"])
                dish.add_ingredient_dependency(
                    ingredient, row["recipe_amount"]
                )
                self.dishes.add(dish)
                self.ingredients.add(ingredient)
        return print(self.dishes, self.ingredients)


menu_data = MenuData("tests/mocks/menu_base_data.csv")
print(menu_data.load_data())