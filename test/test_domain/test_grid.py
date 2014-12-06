
import unittest
from domain.grid import *
import copy
from domain.coordinate import Coordinate
from domain.ship_type import *
from domain.ship import Ship
from domain.direction import *

class TestGrid(unittest.TestCase):
    def testGetColumnLabels(self):
        correct = [1,2,3,4,5,6,7,8,9,10]
        grid = Grid([])
        labels = grid.getColumnLabels()
        self.assertEqual(labels,correct)
    def testGetRowLabels(self):
        correct = ['A','B','C','D','E','F','G','H','I','J']
        grid = Grid([])
        labels = grid.getRowLabels()
        self.assertEqual(labels,correct)
    def testDiffRowCount(self):
        correct = ['A','B','C','D','E','F','G','H','I','J','K']
        grid = Grid([],row_count=11)
        labels = grid.getRowLabels()
        self.assertEqual(labels,correct)
    def testDiffColumnCount(self):
        correct = [1,2,3,4,5,6,7,8,9,10,11]
        grid = Grid([],column_count=11)
        labels = grid.getColumnLabels()
        self.assertEqual(labels,correct)
    def testEmptyFactory(self):
        grid = Grid.factory([],[])
        for row in grid.getRows():
            for cell in row.getCells():
                self.assertEqual(cell,Cell(False))
    def testFactoryWithMiss(self):
        Tests = {2:{2:Cell(True)},3:{3:Cell(True)}}
        Missed = [Coordinate(2,2),Coordinate(3,3)]
        grid = Grid.factory(Missed,[])
        y = 0
        for row in grid.getRows():
            x = 0
            for cell in row.getCells():
                if y in Tests and x in Tests[y]:
                    self.assertEqual(cell,Tests[y][x])
                else:
                    self.assertEqual(cell,Cell(False))
                x += 1
            y += 1
        self.assertEqual(x,10)
        self.assertEqual(y,10)
    def testFactoryWithShip(self):
        destroyer = Destroyer()
        Tests = {2:{2:Cell(False,destroyer)},3:{2:Cell(False,destroyer)}}
        ship = Ship(destroyer,Coordinate(2,2),VerticalDirection())
        ShipCollection = [ship]
        grid = Grid.factory([],ShipCollection)
        y = 0
        for row in grid.getRows():
            x = 0
            for cell in row.getCells():
                if y in Tests and x in Tests[y]:
                    self.assertEqual(cell,Tests[y][x])
                else:
                    self.assertEqual(cell,Cell(False))
                x += 1
            y += 1
        self.assertEqual(x,10)
        self.assertEqual(y,10)
