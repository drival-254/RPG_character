def create_character(name, strength, intelligence, charisma):
    # Validate character name
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # Validate stats
    if not all(type(stat) is int for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"

    if min(strength, intelligence, charisma) < 1:
        return "All stats should be no less than 1"

    if max(strength, intelligence, charisma) > 4:
        return "All stats should be no more than 4"

    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # Create character sheet
    full_dot = "●"
    empty_dot = "○"

    strength_bar = full_dot * strength + empty_dot * (10 - strength)
    intelligence_bar = full_dot * intelligence + empty_dot * (10 - intelligence)
    charisma_bar = full_dot * charisma + empty_dot * (10 - charisma)

    return (
        f"{name}\n"
        f"STR {strength_bar}\n"
        f"INT {intelligence_bar}\n"
        f"CHA {charisma_bar}"
    )
        


print(create_character('ren',3, 3, 1))