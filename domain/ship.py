
class Ship:
    def __init__(self,ShipType,Origin,Direction):
        self.Type = ShipType
        self.Origin = Origin
        self.Direction = Direction
        self.hits = []

    def getType(self):
        return self.Type

    def isHit(self,Coordinate):
        origin_x_y = self.Origin.getXY()
        try_x_y = Coordinate.getXY()
        length = self.Type.getLength()
        return self.Direction.inBetween(origin_x_y,length,try_x_y)

    def shotAt(self,Coordinate):
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

    def getRange(self):
        origin_x_y = self.Origin.getXY()
        length = self.Type.getLength()
        return self.Direction.getRange(origin_x_y,length)

    def isConflict(self,OtherShip):
        r = OtherShip.getRange()
        for x_y in self.getRange():
            if(r.count(x_y)>0):
                return True
        return False

