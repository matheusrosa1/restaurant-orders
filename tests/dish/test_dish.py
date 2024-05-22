from src.models.ingredient import (
    Ingredient,
    Restriction,
)
import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2 ..
def test_dish():
    # Teste de instanciação
    dish1 = Dish("Lasanha", 40)
    dish1.add_ingredient_dependency(Ingredient("massa de lasanha"), 1)
    dish1.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    dish1.add_ingredient_dependency(Ingredient("presunto"), 1)
    assert dish1.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
        Restriction.ANIMAL_MEAT,
        Restriction.GLUTEN,
    }
    assert dish1.get_ingredients() == {
        Ingredient("massa de lasanha"),
        Ingredient("presunto"),
        Ingredient("queijo mussarela"),
    }

    assert dish1.name == "Lasanha"

    # Teste do método __repr__
    assert repr(dish1) == "Dish('Lasanha', R$40.00)"

    # Teste do método __eq__
    dish2 = Dish("Lasanha", 40)
    dish3 = Dish("Pizza", 45)
    assert dish1 == dish2
    assert dish1 != dish3

    # Teste do método __hash__
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    # Testando erros
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Pizza", -5)
    with pytest.raises(TypeError) as excinfo:
        Dish("Pizza", "a")
    assert str(excinfo.value) == "Dish price must be float."
