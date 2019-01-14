### this is a mini game called Lucky

import random

def roll_a_dice():
    return random.randint(1,6)

class Dice(object):
    def __init__(self):
        self.roll()

    def roll(self):
        return random.randint(1, 6)

class Lucky(object):
    def __init__(self):
        self.humanplayer = Dice().roll()
        self.computerplayer = Dice().roll()

        if self.humanplayer > self.computerplayer:
            self.win = True
        elif self.humanplayer < self.computerplayer:
            self.lose = True
        else:
            self.draw = True