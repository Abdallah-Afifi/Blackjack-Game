import random

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = sum([card_value(card['rank']) for card in hand])
    if score > 21 and 'A' in [card['rank'] for card in hand]:
        score -= 10  # Handle the case where there is an Ace and the score exceeds 21
    return score

def card_value(rank):
    if rank in ['K', 'Q', 'J']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)

def display_board(player_hand, computer_hand, reveal_computer_card=False):
    print("\nYour hand:", player_hand, "  Score:", calculate_score(player_hand))
    print("Computer's hand:", computer_hand if reveal_computer_card else [computer_hand[0], '???'])
    print("\n")

def blackjack():
    player_hand = []
    computer_hand = []
    deck = create_deck()

    # Initial deal
    for _ in range(2):
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())

    game_over = False

    while not game_over:
        display_board(player_hand, computer_hand)

        # Check for blackjack
        if calculate_score(player_hand) == 21:
            print("Blackjack! You win!")
            game_over = True
            break
        elif calculate_score(computer_hand) == 21:
            print("Computer has a blackjack. You lose.")
            game_over = True
            break

        # Player's turn
        player_choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
        if player_choice == 'y':
            player_hand.append(deck.pop())
            if calculate_score(player_hand) > 21:
                print("You went over. You lose.")
                game_over = True
        else:
            game_over = True

    # Computer's turn
    while calculate_score(computer_hand) < 17:
        computer_hand.append(deck.pop())

    # Display final hands
    display_board(player_hand, computer_hand, reveal_computer_card=True)

    # Determine the winner
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    if player_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif player_score > computer_score:
        print("You win!")
    elif player_score < computer_score:
        print("You lose.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    blackjack()
