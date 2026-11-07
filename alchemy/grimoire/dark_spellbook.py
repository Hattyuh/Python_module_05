from .dark_validator import validate_ingredient


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if validate_ingredient(ingredients).endswith("INVALID"):
        return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
    return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
