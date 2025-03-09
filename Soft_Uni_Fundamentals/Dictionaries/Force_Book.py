forces = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        force_side, force_user = command.split(" | ")

        if force_side not in forces.keys():
            forces[force_side] = []

        for users in forces.values():
            if force_user not in users:
                forces[force_side].append(force_user)

    if "->" in command:
        force_user, force_side = command.split(" -> ")

        for users in forces.values():
            if force_user in users:
                users.remove(force_user)

        forces[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")


for side, members in forces.items():
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")
