class Ship:
    def __init__(self,ShipType,Origin,Direction):
        self.Type = ShipType
        self.Origin = Origin
        self.Direction = Direction
        self.hits = []

    def getType(self):
        return self.Type

    def isHit(self,Coordinate):
        Coordinates = self.getCoordinates()
        return Coordinates.count(Coordinate) > 0

    def fire(self,Coordinate):
        if(self.isHit(Coordinate)):
            if(not self.hasHit(Coordinate)):
                self.hits.append(Coordinate)
            return True
        return False

    def getHits(self):
        return self.hits

    def hasHit(self,Coordinate):
        return self.hits.count(Coordinate) == 1

    def isSunk(self):
        return self.Type.getLength() <= len(self.hits)

    def getCoordinates(self):
        return self.Origin.range(self.Direction,self.Type.getLength())

    def isConflict(self,OtherShip):
        r = OtherShip.getCoordinates()
        for x_y in self.getCoordinates():
            if(r.count(x_y)>0):
                return True
        return False
