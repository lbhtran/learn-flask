import random

class Card(object):
    def __init__(self, suit, value, isHidden):
        self.suit = suit
        self.value = value
        self.hidden = isHidden

        if (value == 'A'):
            self.pointValue = 11
        elif (value in ['J', 'Q', 'K']):
            self.pointValue = 10
        elif (value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']):
            self.pointValue = int(value)

    def __str__(self):
        ''' The string representation of a card will be formatted between brackets like so:
            [4S] << 4 of Spades
            [KD] << King of Diamonds
            [XX] << Hidden Card (turned over)
        '''

        if (self.hidden):
            return '[XX]'
        else:
            return '[' + str(self.value) + self.suit + ']'

    ### Getters and Setters

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def getPointValue(self):
        return self.pointValue

    def setPointValue(self, pointValue):
        self.pointValue = pointValue

    ### Misc method for Game Check
    def isHidden(self):
        return self.hidden

    def hideCard(self):
        self.hidden = True

    def revealCard(self):
        self.hidden = False

    def isAce(self):
        return self.value == 'A'

class Deck(object):
    '''
    The Deck Object is a representation of 52 card objects.
    When instantiated, this deck's list of cards is mutable, as it is a list.
    Cards can be randomly selected, then destroyed from the deck list so that
    it represents a card no longer being in the deck
    '''

    def __init__(self):
        cardsInDeck = []
        suits = ['S', 'H', 'D', 'C']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                cardsInDeck.append(Card(suit, value, False))
        self.cardsInDeck = cardsInDeck[:]

    def __str__(self):
        return 'The Deck has ' + str(len(self.cardsInDeck)) + ' cards left.'

    def dealCard(self):
        card = random.choice(self.cardsInDeck)
        self.cardsInDeck.remove(card)
        return card

class Hand(object):
    def __init__(self):
        self.cards = []
        self.value = 0

    def addCard(self, card):
        self.cards.append(card)

    def getHandValue(self):
        for card in self.cards:
            self.value += card.pointValue

class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        self.hand.addCard(self.deck.dealCard())
        self.hand.addCard(self.deck.dealCard())

