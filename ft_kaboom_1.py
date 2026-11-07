from alchemy.grimoire.dark_spellbook import dark_spell_record


if __name__ == "__main__":
    spell_name: str = "Dark"
    ingredients: str = "bats eyeball"
    print(
        "=== Kaboom 1 ===\n"
        "Using grimoire module directly\n"
        "Testing dark spell: "
        f"{dark_spell_record(spell_name, ingredients)}"
    )
