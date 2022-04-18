from art import logo
from random import choice
import replit

game = True

while game:

    if input("\nDo you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == "n":
        game = False
    else:
        replit.clear()
        print(logo)

        computer_cards = []
        user_cards = []
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_score = 0
        computer_score = 0
        players = ["user", "pc"]


        def deal():
            for n in range(2):
                computer_cards.append(choice(cards))
                user_cards.append(choice(cards))


        def count_score():
            global user_score, computer_score
            user_score = sum(user_cards)
            computer_score = sum(computer_cards)


        def print_score():
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}\n")


        def check_blackjack():
            if computer_score == 21 or user_score == 21:
                return True


        def check_winner():
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            if computer_score == 21:
                if len(computer_cards) == 2:
                    print("Computer has BlackJack! Computer Wins!")
                else:
                    print("Computer Wins!")
            elif user_score == 21:
                if len(user_cards) == 2:
                    print("User has BlackJack! User Wins!")
                else:
                    print("User Wins!")
            elif user_score > 21:
                print("User has Bust! Computer Wins!")
            elif computer_score > 21:
                print("Computer has Bust! User Wins!")
            elif computer_score == user_score:
                print("It's a draw!")
            elif user_score > computer_score:
                print("User Wins!")
            else:
                print("Computer Wins!")


        def user_another_card():
            user_cards.append(choice(cards))


        def computer_another_card():
            computer_cards.append(choice(cards))


        def check_for_ace():
            if sum(computer_cards) > 21 or sum(user_cards) > 21:
                if 11 in computer_cards:
                    index = computer_cards.index(11)
                    computer_cards[index] = 1
                if 11 in user_cards:
                    index = user_cards.index(11)
                    user_cards[index] = 1
                else:
                    pass


        deal()
        check_for_ace()
        count_score()
        print_score()

        if check_blackjack():
            check_winner()
        else:
            check_for_ace()

            while sum(user_cards) < 21:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if another_card == "n":
                    break
                else:
                    user_another_card()
                    check_for_ace()
                    count_score()
                    print_score()

            while sum(computer_cards) < 17:
                computer_another_card()
                check_for_ace()
                count_score()
            check_winner()
