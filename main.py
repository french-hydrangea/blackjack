from os import system, name


def clear():
    """clears the console"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def deal_card():
    """Adds a card to the user's or computer's hand"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    import random
    card = random.choice(cards)
    return card


while True:

    play = input("Do you want to play a game of blackjack? y/n ")
    if play == 'n':
        break

    while play == "y":
        clear()
        your_cards = []
        comp_cards = []
        for i in range(0, 2):
            your_cards.append(deal_card())
            comp_cards.append(deal_card())
            i += 1
        your_total = sum(your_cards)
        comp_total = comp_cards[0] + comp_cards[1]
        comp_first = comp_cards[0]


        def compare_score():
            """checks if the user or computer has a blackjack and if the user's score went over 21"""
            your_total = sum(your_cards)
            if comp_total == 21:
                print(f"Your final hand: {your_cards}, your final score: {your_total}")
                print(f"Computer's final hand: {comp_cards}, computer's final score: {comp_total}")
                print("Computer has a blackjack. You lose.")
            elif your_total == 21:
                print(f"Your final hand: {your_cards}, your final score: {your_total}")
                print(f"Computer's final hand: {comp_cards}, computer's final score: {comp_total}")
                print("You have a blackjack. You win!")

            elif your_total > 21:
                if 11 in your_cards:
                    your_cards[your_cards.index(11)] = 1
                    your_total = sum(your_cards)
                    if your_total > 21:
                        print(f"Your final hand: {your_cards}, your final score: {your_total}")
                        print(f"Computer's final hand: {comp_cards}, computer's final score: {comp_total}")
                        print("You went over. You lose.")
                print(f"Your final hand: {your_cards}, your final score: {your_total}")
                print(f"Computer's final hand: {comp_cards}, computer's final score: {comp_total}")
                print("You went over. You lose.")


        print(f"Your cards: {your_cards}, your current score: {your_total}")
        print(f"Computer's first card: {comp_first}")
        compare_score()
        if comp_total == 21:
            break
        elif your_total == 21:
            break
        elif your_total > 21:
            if 11 in your_cards:
                your_cards[your_cards.index(11)] = 1
                your_total = sum(your_cards)
                if your_total > 21:
                    break
            break

        add_card = input("Type 'y' to get another card, type 'n' to pass:")

        while add_card == 'y':
            your_cards.append(deal_card())
            your_total = sum(your_cards)
            print(f"Your cards: {your_cards}, your current score: {your_total}")
            print(f"Computer's first card: {comp_first}")
            compare_score()
            if comp_total == 21:
                break
            elif your_total == 21:
                break
            elif your_total > 21:
                if 11 in your_cards:
                    your_cards[your_cards.index(11)] = 1
                    your_total = sum(your_cards)
                    if your_total > 21:
                        break
                break

            add_card = input("Type 'y' to get another card, type 'n' to pass:")

        if add_card == 'n':
            while comp_total < 17:
                comp_cards.append(deal_card())
                comp_total = sum(comp_cards)
            print(f"Your final hand: {your_cards}, your final score: {your_total}")
            print(f"Computer's final hand: {comp_cards}, computer's final score: {comp_total}")

            if comp_total > 21:
                print("The computer went over 21. You win!")
                break
            elif your_total == comp_total:
                print("It's a draw.")
                break
            elif your_total < comp_total:
                print("You lose.")
                break
            elif your_total > comp_total:
                print("You win!")
                break
