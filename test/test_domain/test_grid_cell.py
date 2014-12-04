import unittest
from domain.grid import Cell
from domain.ship_type import *

class TestGridCell(unittest.TestCase):
    def testNotIsMiss(self):
        ship = Battleship()
        cell = Cell(False,ship)
        self.assertFalse(cell.isMiss())
        cell = Cell(False)
        self.assertFalse(cell.isMiss())
        cell = Cell(True,ship)
        self.assertFalse(cell.isMiss())
    def testIsMiss(self):
        cell = Cell(True)
        self.assertTrue(cell.isMiss())
    def testIsHit(self):
        ship = Battleship()
        cell = Cell(True,ship)
        self.assertTrue(cell.isHit())
    def testHasShip(self):
        ship = Battleship()
        cell = Cell(True,ship)
        self.assertTrue(cell.hasShip())
        cell = Cell(True)
        self.assertFalse(cell.hasShip())
    def testGetShipType(self):
        ship = Battleship()
        cell = Cell(True,ship)
        self.assertEqual(cell.getShipType(),ship)
        cell = Cell(True)
        self.assertIsNone(cell.getShipType())
    def testIsEqual(self):
        ship1 = Battleship()
        ship2 = Battleship()
        self.assertEqual(Cell(False,ship1),Cell(False,ship2))
        self.assertEqual(Cell(True,ship1),Cell(True,ship2))
        self.assertEqual(Cell(True),Cell(True))
        self.assertEqual(Cell(False),Cell(False))
        self.assertEqual(Cell(),Cell(False))
    def testIsNotEqual(self):
        ship1 = Battleship()
        ship2 = Battleship()
        self.assertNotEqual(Cell(True,ship1),Cell(False,ship2))
        self.assertNotEqual(Cell(True),Cell(True,ship2))
        self.assertNotEqual(Cell(False),Cell(True))
        self.assertNotEqual(Cell(),Cell(True))
