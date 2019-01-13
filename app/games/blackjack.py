class Card(object):
    def __init__(self, suit, value, isHidden):
        self.suit = suit
        self.value = value
        self.hidden =  isHidden

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