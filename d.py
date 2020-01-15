import random

hand = []
banished = []
grave = []
mfield = []
stfield = []
pendzone = []


def draw(amount):
    shuffle()
    for i in range(amount):
        hand.append(deck[0])
        del deck[0]


def shuffle():
    random.shuffle(deck)


def importdeck(filename):
    with open(filename) as f:
        deck = [line.rstrip() for line in f]
        return deck

def banish(amount):
    shuffle()
    for i in range(amount):
        banished.append(deck[0])
        del deck[0]

def send(id):
    deck.remove(id)
    grave.append(id)

deck = importdeck("luna.txt")









