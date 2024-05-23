import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self._load_data()

    def _load_data(self) -> None:
        dishes_dict = {}
        try:
            with open(self.source_path, newline="") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    dish_name, price, ingredient_name, amount = row
                    price = float(price)
                    amount = int(amount)

                    if dish_name not in dishes_dict:
                        dish = Dish(dish_name, price)
                        dishes_dict[dish_name] = dish
                        self.dishes.add(dish)
                    else:
                        dish = dishes_dict[dish_name]

                    ingredient = Ingredient(ingredient_name)
                    dish.add_ingredient_dependency(ingredient, amount)

        except FileNotFoundError:
            print(f"Error: File '{self.source_path}' not found.")


if __name__ == "__main__":
    menu_data = MenuData("tests/mocks/menu_base_data.csv")
    for dish in menu_data.dishes:
        print("Dish:", dish)
        print("Dish recipe:", dish.recipe)
        print("Dish restrictions:", dish.get_restrictions())
        print("Dish ingredients:", dish.get_ingredients())
        print("Dish price", dish.price)
