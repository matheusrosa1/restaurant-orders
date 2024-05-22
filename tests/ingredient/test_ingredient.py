from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Teste de instanciação
    queijo_mussarela = Ingredient("queijo mussarela")
    assert queijo_mussarela.name == "queijo mussarela"
    assert queijo_mussarela.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    # Teste do método __repr__
    manteiga = Ingredient("manteiga")
    assert repr(manteiga) == "Ingredient('manteiga')"

    # Teste do método __eq__
    camarao1 = Ingredient("camarão")
    camarao2 = Ingredient("camarão")
    presunto = Ingredient("presunto")
    assert camarao1 == camarao2
    assert camarao1 != presunto

    # Teste do método __hash__
    creme_de_leite1 = Ingredient("creme de leite")
    creme_de_leite2 = Ingredient("creme de leite")
    frango = Ingredient("frango")
    assert hash(creme_de_leite1) == hash(creme_de_leite2)
    assert hash(creme_de_leite1) != hash(frango)
