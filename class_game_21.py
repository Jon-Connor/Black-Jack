import random


class Game:
    # метод раздает карты
    @staticmethod
    def card_deck():
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
        card = random.choice(deck)
        return card

    # метод считает сумму карт
    @staticmethod
    def sum_cards(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    # метод определяет кто победил
    @staticmethod
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

    # метод управляет игрой
    def play_game(self):
        total_user = None
        total_comp = None
        cards_user = []
        cards_comp = []
        game_over = False
        for _ in range(2):
            cards_user.append(self.card_deck())
            cards_comp.append(self.card_deck())
        print("Раздача карт")
        while not game_over:
            total_user = self.sum_cards(cards_user)
            total_comp = self.sum_cards(cards_comp)
            print(f"Ваши карты: {cards_user}, Сумма карт: {total_user}")
            print(f"Карты компьютера: {cards_comp[0]}")
            if total_user == 0 or total_comp == 0 or total_user > 21:
                game_over = True
            else:
                continue_user = input("Еще карту?[д/н]")
                if continue_user == "д":
                    cards_user.append(self.card_deck())
                else:
                    game_over = True
        while total_comp != 0 and total_comp < 17:
            cards_comp.append(self.card_deck())
            total_comp = self.sum_cards(cards_comp)
        print(f"Карты компьютера: {cards_comp}, сумма {total_comp}")
        print(self.result(total_user, total_comp))


while input("хотите сыграть еще? [д/н]") == "д":
    Game().play_game()
