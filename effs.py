import random


def draw(deck,hand,amount):
    for i in amount:
        hand.append(deck[i])
        del deck[i]



def shuffle(deck):
    random.shuffle(deck)


