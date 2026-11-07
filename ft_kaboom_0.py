from alchemy.grimoire.light_spellbook import light_spell_record


if __name__ == "__main__":
    spell_name: str = "Fantasy"
    ingredients: str = "Earth, wind and fire"
    print(
        "=== Kaboom 0 ===\n"
        "Using grimoire module directly\n"
        "Testing light spell: "
        f"{light_spell_record(spell_name, ingredients)}"
    )
