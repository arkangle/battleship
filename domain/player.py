import random

class Player:
    def __init__(self,name,battlefield):
        self.name = name;
        self.battlefield = battlefield;

    def getName(self):
        return self.name

    def getBattlefield(self):
        return self.battlefield
