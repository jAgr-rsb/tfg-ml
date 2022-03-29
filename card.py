class Card(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + "-" + self.suit

    @staticmethod
    def get_card_value(self):
        if self.value == "TWO":
            return 2
        elif self.value == "THREE":
            return 3
        elif self.value == "FOUR":
            return 4
        elif self.value == "FIVE":
            return 5
        elif self.value == "SIX":
            return 6
        elif self.value == "SEVEN":
            return 7
        elif self.value == "EIGHT":
            return 8
        elif self.value == "NINE":
            return 9
        elif self.value == "TEN" or self.value == "JACK" or self.value == "QUEEN" or self.value == "KING":
            return 10
        elif self.value == "ACE":
            return 11
        else:
            return 0
