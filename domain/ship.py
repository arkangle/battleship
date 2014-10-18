
class Ship:
    def __init__(self,ShipType,Origin,Direction):
        self.Type = ShipType
        self.Origin = Origin
        self.Direction = Direction

    def getEndXY(self):
        length = self.Type.getLength()
        x_y = self.Origin.getXY()
        end_x_y = self.Direction.getEndXY(x_y,length)
        return end_x_y

    def isHit(self,Coordinate):
        origin_x_y = self.Origin.getXY()
        try_x_y = Coordinate.getXY()
        length = self.Type.getLength()
        return self.Direction.inBetween(origin_x_y,length,try_x_y)
