
class Coordinate:
    rows = ['A','B','C','D','E','F','G','H','I','J']
    columns = range(1,11)
    def __init__(self,x_y):
        if(x_y[0] < 0 or x_y[0] > 9):
            raise ValueError("column/x is Invalid: %s" % x_y[0])
        if(x_y[1] < 0 or x_y[1] > 9):
            raise ValueError("row/y is Invalid: %s" % x_y[1])
        self.x=x_y[0]
        self.y=x_y[1]

    @staticmethod
    def Factory(row_column):
        y = Coordinate.rows.index(row_column[0])
        x = Coordinate.columns.index(row_column[1])
        return Coordinate((x,y))

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
