import string
from domain.coordinate import Coordinate
class Grid:
    row_count = 10
    column_count = 10
    rows = []
    @staticmethod
    def factory(Missed,ShipCollection):
        grid = {}
        for Coor in Missed:
            y = Coor.getY()
            x = Coor.getX()
            if not y in grid:
                grid[y] = {}
            grid[y][x] = Cell(True)
        for ship in ShipCollection:
            for (x,y) in ship.getLocation():
                if not y in grid:
                    grid[y] = {}
                grid[y][x] = Cell(ship.hasHit(Coordinate((x,y))),ship.getType())

        Rows = []
        labels = list(string.ascii_uppercase)
        for r in range(Grid.row_count):
            cells = []
            for c in range(Grid.column_count):
                if r in grid and c in grid[r]:
                    cells.append(grid[r][c])
                else:
                    cells.append(Cell(False))
            Rows.append(Row(labels[r],cells))
        return Grid(Rows)

    def __init__(self,rows,row_count=10,column_count=10):
        self.rows = rows
        self.row_count=row_count
        self.column_count=column_count

    def getColumnLabels(self):
        labels = list(range(1,self.column_count+1))
        return labels

    def getRowLabels(self):
        labels = list(string.ascii_uppercase)[0:self.row_count]
        return labels

    def getRows(self):
        return self.rows

class Row:
    label = ""
    cells = []
    def __init__(self,label,cells):
        self.label = label
        self.cells = cells

    def getLabel(self):
        return self.label

    def getCells(self):
        return self.cells

class Cell:
    ShipType = None
    shotAt = False
    empty = True
    def __init__(self,shotAt=False,ShipType=None):
        self.shotAt = shotAt
        self.ShipType = ShipType
        if self.ShipType == None:
            self.empty = True
        else:
            self.empty = False

    def isMiss(self):
        return (self.empty) and self.shotAt

    def isHit(self):
        return (not self.empty) and self.shotAt

    def hasShip(self):
        return not self.empty

    def getShipType(self):
        return self.ShipType

    def __eq__(self,Other):
        return (self.isMiss() == Other.isMiss()
           and self.isHit() == Other.isHit()
           and self.ShipType == Other.getShipType())
    def __ne__(self,Other):
        return not self.__eq__(Other)
