import elements
from .. import elements as alchemy_elements
from .. import potions


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"’{alchemy_elements.create_air()}’ and "
        f"’{potions.strength_potion()}’ mixed with "
        f"’{elements.create_fire()}’."
    )
