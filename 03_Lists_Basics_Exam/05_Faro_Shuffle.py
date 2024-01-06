def faro_shuffle(deck, num_shuffles):
    # Split the deck into two halves
    middle = len(deck) // 2
    first_half = deck[:middle]
    second_half = deck[middle:]

    # Perform faro shuffle for the specified number of times
    for _ in range(num_shuffles):
        shuffled_deck = []
        for card1, card2 in zip(first_half, second_half):
            shuffled_deck.append(card1)
            shuffled_deck.append(card2)

        # Update halves for the next iteration
        first_half = shuffled_deck[:middle]
        second_half = shuffled_deck[middle:]

    return shuffled_deck

# Example usage:
input_string = input()
num_shuffles = int(input())

cards = input_string.split()
shuffled_deck = faro_shuffle(cards, num_shuffles)

print(shuffled_deck)
