from cards import Card, Deck, Hand

def game():
    play_again = True
    while play_again:
#Create and shuffle the deck
        deck = Deck()
        deck.shuffle()
#Create hands for player and the dealer
        player_hand = Hand()
        dealer_hand = Hand()

#Deal initial cards (2 cards each)
#Show players initial hand and dealer's face up card
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        print("\n--- Initial Deal ---")
        print(f"Your cards: {player_hand.cards[0].rank} of {player_hand.cards[0].suit}, {player_hand.cards[1].rank} of {player_hand.cards[1].suit}")
        print(f"Your total: {player_hand.get_value()}")
        print(f"\nDealer showing: {dealer_hand.cards[0].rank} of {dealer_hand.cards[0].suit}")
        print(f"Dealer's other card is face down\n")

#Player hits or stands
        if player_hand.get_value() == 21:
            print("Blackjack! You Win!")
            response = input("\nPlay Again? (y/n): ").lower()
            if response != "y":
                play_again = False
            continue


        while player_hand.get_value() < 21:
            action = input("Hit or Stand?-(H or S) ").lower()
            if action == "h":
                new_card = deck.deal()
                player_hand.add_card(new_card)
                print(f'Your new card: {new_card.rank} of {new_card.suit}')
                print(f"Your total: {player_hand.get_value()}")

                if player_hand.get_value() == 21:
                    print("You have 21!")
                    break
                if player_hand.get_value() > 21:
                    print("You Bust! Game Over.")
                    break
            elif action == "s":
                break
            else:
                print("Invalid Input")
#Dealers reveals second card, if under 16 dealer must hit
        print(f"\nDealer reveals: {dealer_hand.cards[1].rank} of {dealer_hand.cards[1].suit}")
        print(f"Dealer's total: {dealer_hand.get_value()}")

        while dealer_hand.get_value() < 17:
            new_card = deck.deal()
            dealer_hand.add_card(new_card)
            print(f'Dealer Draws: {new_card.rank} of {new_card.suit}')
            print(f"Dealer's total: {dealer_hand.get_value()}")

        if dealer_hand.get_value() > 21:
            print("Dealer Busts! You Win")
            response = input("Play Again? (y/n) ").lower()
            if response != "y":
                play_again = False
            continue

        player_total = player_hand.get_value()
        dealer_total = dealer_hand.get_value()


        print(f"\nFinal Results:")
        print(f"Your total: {player_total}")
        print(f"Dealer's total: {dealer_total}")

        if 21 >= player_total > dealer_total:
            print("You win!")
        elif player_total < dealer_total <= 21:
            print("Dealer wins!")
        elif player_total == dealer_total:
            print("Push! It's a tie.")


        response = input("Play Again? (y/n) ").lower()
        if response != "y":
            play_again = False
#Determine winner


if __name__ == "__main__":
    game()
