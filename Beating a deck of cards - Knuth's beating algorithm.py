SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
import random
rank = random.randrange(0, len(RANKS))
suit = random.randrange(0, len(SUITS))
print(RANKS[rank] + 'of' + SUITS[suit])
deck  = []
for rank in RANKS:
    for suit in SUITS:
        card = rank + 'of' + suit
        deck +=[card]
n= len(deck)
for i in range(n):
    r = random.randrange(0, i+1)
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp
    
        
