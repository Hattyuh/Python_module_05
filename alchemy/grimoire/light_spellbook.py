def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredient
    if validate_ingredient(ingredients).endswith("INVALID"):
        return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
    return f"Spell recorded: {spell_name} ({ingredients} - VALID)"

