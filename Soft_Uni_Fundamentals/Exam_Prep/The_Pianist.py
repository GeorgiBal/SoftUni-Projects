pieces = int(input())
pieces_themselves = {}

for index in range(pieces):
    piece, composer, key = input().split("|")

    pieces_themselves[piece] = [composer, key]


while True:
    command = input()

    if command.startswith("Stop"):
        break
    elif command.startswith("Add"):
        action, piece, composer, key = command.split("|")
        if piece not in pieces_themselves:
            pieces_themselves[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command.startswith("Remove"):
        action, piece = command.split("|")
        if piece in pieces_themselves:
            del pieces_themselves[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command.startswith("ChangeKey"):
        action, piece, new_key = command.split("|")
        if piece in pieces_themselves:
            pieces_themselves[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, values in pieces_themselves.items():
    print(f"{piece} -> Composer: {values[0]}, Key: {values[1]}")