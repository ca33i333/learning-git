# Input
deck = input().split()
index_to_cut, num_to_draw = map(int, input().split())

# Define function
def deck_bottom_draw(deck, index_to_cut, num_to_draw):

    # Cut the deck at a given index: move the suffix to the front.
    deck = deck[index_to_cut:] + deck[:index_to_cut]

    # Draw a given number of cards from the bottom of the cut deck.
    hand = deck[-num_to_draw:]
    deck = deck[:-num_to_draw]
    
    # Reverse the drawn cards (your hand)
    hand.reverse()

    print(*deck)
    print(*hand)

deck_bottom_draw(deck, index_to_cut, num_to_draw)
