
class ShipType:
    def __init__(self,name,length):
        self.name=name
        self.length=length

    def getLength(self):
        return self.length

    def getName(self):
        return self.name

    def __eq__(self,Other):
        return self.name == Other.getName() and self.length == Other.getLength()

    def __ne__(self,Other):
        return not self.__eq__(Other)

class Battleship(ShipType):
    def __init__(self):
        ShipType.__init__(self,"Battleship",4)

class Carrier(ShipType):
    def __init__(self):
        ShipType.__init__(self,"Carrier",5)

class Cruiser(ShipType):
    def __init__(self):
        ShipType.__init__(self,"Cruiser",3)

class Destroyer(ShipType):
    def __init__(self):
        ShipType.__init__(self,"Destroyer",2)

class Submarine(ShipType):
    def __init__(self):
        ShipType.__init__(self,"Submarine",3)

