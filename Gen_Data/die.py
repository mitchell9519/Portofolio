from random import randint

class Die:
    """Simulates a dice"""

    def __init__(self, num_sides = 6):
        """assume a six sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return num from sides"""
        return randint(1,self.num_sides)