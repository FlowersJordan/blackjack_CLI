# Blackjack Game

A command-line Blackjack game built in Python using object-oriented programming principles.

## Description

This is a fully functional Blackjack game where you play against a dealer. The game follows standard Blackjack rules with proper handling of Aces (counting as 1 or 11), dealer hitting until 17, and the ability to play multiple hands.

## Features

- Object-oriented design with Card, Deck, and Hand classes
- Proper Ace handling (automatically adjusts between 1 and 11)
- Dealer follows standard rules (must hit until 17 or higher)
- Color-coded terminal output for better visibility
- Continuous play - play multiple hands without restarting
- Win/loss/push detection

## Project Structure

- `cards.py` - Contains Card, Deck, and Hand classes
- `blackjack.py` - Main game logic and player interaction

## How to Run

1. Install the required package:
```
pip install random
```

2. Run the game:
```
python blackjack.py
```

## How to Play

1. You and the dealer are each dealt 2 cards
2. You can see both of your cards and only one of the dealer's cards
3. Choose to "Hit" (H) to draw another card or "Stand" (S) to keep your current hand
4. Try to get as close to 21 as possible without going over
5. If you bust (go over 21), you lose immediately
6. If you stand, the dealer reveals their hidden card and must hit until reaching 17 or higher
7. Whoever has the higher total without busting wins

## Game Rules

- Number cards (2-10) are worth their face value
- Face cards (J, Q, K) are worth 10
- Aces are worth 11, but automatically count as 1 if that keeps you from busting
- Blackjack (21 with initial 2 cards) is an instant win
- Dealer must hit on 16 or below, must stand on 17 or above

## What I Learned

- Object-oriented programming concepts (classes, methods, inheritance)
- Organizing code across multiple files and importing modules
- Complex game state management with multiple conditions
- Nested loops and control flow (break, continue)
- Handling edge cases (Ace values, bust conditions, blackjack)
- Building reusable, modular code components