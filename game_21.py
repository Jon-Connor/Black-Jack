import random


# функция будет случайно раздавать карту из колоды
def card_deck():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    card = random.choice(cards)
    return card


# функция будет возвращать сумму карт
def sum_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# функция будет определять кто победит
def result(result_user, result_comp):
    if result_comp == result_user:
        return "Ничья"
    elif result_comp == 0:
        return "ВЫ проиграли у компьютера Black Jack"
    elif result_user == 0:
        return "ВЫ выиграли у вас Black Jack"
    elif result_comp > 21:
        return "Вы выиграли, у компьютера перебор"
    elif result_user > 21:
        return "Вы проиграли, у вас перебор"
    elif result_user > result_comp:
        return "Вы выиграли"
    else:
        return "Вы проиграли"


def game():
    user_cards = []
    comp_cards = []
    game_over = False
    sum_cards_comp = None
    sum_cards_user = None

    # раздача
    for _ in range(2):
        user_cards.append(card_deck())
        comp_cards.append(card_deck())
    print("карты на столе")
    while not game_over:
        sum_cards_user = sum_cards(user_cards)
        sum_cards_comp = sum_cards(comp_cards)
        print(f"карты компьютера {comp_cards[0]}")
        print(f"ваши карты {user_cards} Ваш сумма карт составляет: {sum_cards_user}")
        if sum_cards_comp == 0 or sum_cards_user == 0 or sum_cards_user > 21:
            game_over = True
        else:
            cont_user = input("еще карту? [д/н]:")
            if cont_user == "д":
                user_cards.append(card_deck())
            else:
                game_over = True

    while sum_cards_comp != 0 and sum_cards_comp < 17:
        comp_cards.append(card_deck())
        sum_cards_comp = sum_cards(comp_cards)
    print(f"карты компьютера {comp_cards} Сумма компьютера составляет: {sum_cards_comp}")
    print(result(sum_cards_user, sum_cards_comp))


while input("хотите сыграть [д/н]") == "д":
    game()
