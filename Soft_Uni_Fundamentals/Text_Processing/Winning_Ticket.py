def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    winning_symbols = ['@', '#', '$', '^']
    half1 = ticket[:10]
    half2 = ticket[10:]

    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            repetition = match_symbol*uninterrupted_match_length
            if repetition in half1 and repetition in half2:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                else:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:

    print(check_ticket(ticket))




