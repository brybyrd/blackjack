cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
deck = []
 
for suit in suits:
    for card in cards:
        deck.append(Card(suits_values[suit], card, cards_values[card]))
         
         def blackjack_game(deck):