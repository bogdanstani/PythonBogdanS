import random
from random import choice


class Card(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f' {self.value} of {self.suit}'


def new_deck_of_cards():
    value = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suit = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

    list_of_new_cards = list()

    for v in value:
        for s in suit:
            list_of_new_cards.append(Card(v, s))

    return Deck(list_of_new_cards)


class Deck(object):

    def __init__(self, list_of_cards):
        self.list_of_cards = list_of_cards

    def deal_card_from_deck(self):
        deal_card = choice(self.list_of_cards)
        print(f' {deal_card}  was deal  and after removed from deck')
        self.list_of_cards.remove(deal_card)

        # return deal_card

    def shuffle_deck(self):
        shuffle_list = self.list_of_cards
        random.shuffle(shuffle_list)
        return shuffle_list

    def __str__(self):
        string_for_join = ''
        for each in self.list_of_cards:
            # print(each)
            string_for_join += str(each) + '\n'

        return string_for_join


if __name__ == '__main__':
    new_deck = new_deck_of_cards()

    new_deck.deal_card_from_deck()
    print(f'the deck after dealing is:\n', new_deck)

    print(f'shuffling the deck :\n', Deck(new_deck.shuffle_deck()))