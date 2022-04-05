import card as c


class Deck(object):

    def __init__(self):
        self.cards = []
        self.value = 0

    def set_cards(self):
        suits = ["HEARTS", "DIAMONDS", "SPADES", "CLOVERS"]
        values = ["TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN",
         "JACK", "QUEEN", "KING", "ACE"]
        for x in suits:
            for y in values:
                card = c.Card(x, y)
                self.cards.append(card)

    def get_top_card(self):
        return self.cards[-1]

    def remove_top_card(self):
        self.cards.remove(self.cards[-1])

    def set_hand_value(self):
        ace_count = 0
        total = 0
        for x in self.cards:
            if x.value == "ACE":
                ace_count += 1
            else:
                total += x.get_card_value(x)
        for x in range (ace_count):
            if (total+11) > 21:
                total+=1
            else:
                total+=11
        self.value = total

    def deal(self, deal_deck, cards_to_deal):
        for x in range (cards_to_deal):
            self.cards.append(deal_deck.get_top_card())
            deal_deck.remove_top_card()
        self.set_hand_value()

    def show_hand(self, dealer):
        if dealer:
            print("Dealers hand:")
            for card in self.cards:
                print(card)
            print("Dealer hand value:",self.value)
        else:
            print("Players hand:")
            for card in self.cards:
                print(card)
            print("Player hand value:",self.value)
   
    def check_blackjack(self):
        first_card = self.cards[0]
        second_card = self.cards[1]
        face_cards = ["TEN", "JACK", "QUEEN", "KING"]
        if (first_card.value == "ACE" and second_card.value in face_cards) or (first_card.value in face_cards and second_card.value == "ACE"):
            return True
        else:
            return False

    def reset(self):
        self.cards.clear()
        self.value = 0