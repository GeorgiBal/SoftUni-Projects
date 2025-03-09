heroes = {}

while True:
    command = input()

    if command.startswith("End"):
        break
    elif command.startswith("Enroll"):
        action, hero_name = command.split()
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif command.startswith("Learn"):
        action, hero_name,  spell_name = command.split()
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)
    elif command.startswith("Unlearn"):
        action, hero_name,  spell_name = command.split()
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)


print("Heroes:")
for hero, spells in heroes.items():
    spells = ", ".join(spells)
    print(f"== {hero}: {spells}")
