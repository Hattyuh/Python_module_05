from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredient(ingredients: str) -> str:
    for ingredient in ingredients.split():
        if ingredient.lower() in light_spell_allowed_ingredients():
            return f"{ingredients}VALID"
    return f"{ingredients}INVALID"
