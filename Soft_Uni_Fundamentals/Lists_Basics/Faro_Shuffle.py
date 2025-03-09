deck = input().split()
shuffles = int(input())

deck_size = len(deck)

for i in range(shuffles):
    shuffled_deck = []
    half_size = deck_size // 2

    for j in range(half_size):
        shuffled_deck.append(deck[j])
        shuffled_deck.append(deck[j + half_size])

    deck = shuffled_deck
print(deck)

