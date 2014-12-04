import unittest
from domain.grid import Row

class TestGridRow(unittest.TestCase):
    def testGetLabel(self):
        cells = []
        row = Row("A",cells)
        test = row.getLabel()
        self.assertEqual(test,"A")
    def testGetCells(self):
        cells = [0,0,0,0,1,1,1,0,0,0]
        row = Row("A",cells)
        test = row.getCells()
        self.assertEqual(test,cells)
