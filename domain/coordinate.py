class Coordinate:
    rows = ['A','B','C','D','E','F','G','H','I','J']
    columns = range(1,11)
    def __init__(self,x,y):
        self.x=x
        self.y=y

    @staticmethod
    def Factory(row,column):
        y = Coordinate.rows.index(row)
        x = Coordinate.columns.index(column)
        return Coordinate(x,y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getXY(self):
        return (self.getX(),self.getY())

    def getRow(self):
        return Coordinate.rows[self.y]

    def getColumn(self):
        return Coordinate.columns[self.x]

    def getRowColumn(self):
        return (self.getRow(),self.getColumn())

    def __eq__(self,Other):
        return self.x == Other.getX() and self.y == Other.getY()

    def __ne(self,Other):
        return not self.__eq__(Other)

    def range(self,Direction,length):
        Coor = self
        rc = [Coor]
        for i in range(length-1):
            x_y = Direction.nextXY(Coor.getXY())
            Coor = Coordinate(x_y[0],x_y[1])
            rc.append(Coor)
        return rc
