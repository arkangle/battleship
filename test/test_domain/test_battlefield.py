
import unittest
from domain.battlefield import *
from domain.coordinate import Coordinate
from domain.direction import *
from domain.ship_type import *
from domain.ship import Ship

class TestBattlefield(unittest.TestCase):
    def setUp(self):
        self.Battlefield = Battlefield()
    
    def testAddShip(self):
        TestShip = self.getGenericShip(1,1,"H","Horiz",4)
        self.Battlefield.addShip(TestShip)

    def testAddShipConflict(self):
        HTestShip = self.getGenericShip(1,1,"H","Horiz",4)
        self.Battlefield.addShip(HTestShip)
        VTestShip = self.getGenericShip(2,0,"V","Vert",4)
        self.assertRaisesRegex(ValueError,"Ship in the way",self.Battlefield.addShip,VTestShip)

    def testAddShipTypeUsed(self):
        HTestShip = self.getGenericShip(1,1,"H","Ship",4)
        self.Battlefield.addShip(HTestShip)
        VTestShip = self.getGenericShip(0,0,"V","Ship",4)
        self.assertRaisesRegex(ValueError,"Ship Type Already Used",self.Battlefield.addShip,VTestShip)

    def testShotAtHit(self):
        self.fillBattlefield()
        ship = self.Battlefield.shotAt(Coordinate(0,3))
        
    def testShotAtHitSink(self):
        self.fillBattlefield()
        for i in range(1,5):
            ship = self.Battlefield.shotAt(Coordinate(i,1))
            self.assertFalse(ship.isSunk())
        ship = self.Battlefield.shotAt(Coordinate(5,1))
        self.assertTrue(ship.isSunk())

    def testShotAtMiss(self):
        self.fillBattlefield()
        Attempt = Coordinate(0,0)
        self.assertIsNone(self.Battlefield.shotAt(Attempt))
        Attempt = Coordinate(9,9)
        self.assertIsNone(self.Battlefield.shotAt(Attempt))
        Attempt = Coordinate(0,1)
        self.assertIsNone(self.Battlefield.shotAt(Attempt))
        Attempt = Coordinate(6,1)
        self.assertIsNone(self.Battlefield.shotAt(Attempt))

    def testAreAllSunk(self):
        HTestShip = self.getGenericShip(1,1,"H","HorizShip",3)
        self.Battlefield.addShip(HTestShip)
        VTestShip = self.getGenericShip(0,0,"V","VertShip",2)
        self.Battlefield.addShip(VTestShip)
        self.assertFalse(self.Battlefield.areAllSunk())
        ship = self.Battlefield.shotAt(Coordinate(1,1))
        self.assertFalse(self.Battlefield.areAllSunk())
        ship = self.Battlefield.shotAt(Coordinate(2,1))
        self.assertFalse(self.Battlefield.areAllSunk())
        ship = self.Battlefield.shotAt(Coordinate(3,1))
        self.assertFalse(self.Battlefield.areAllSunk())
        ship = self.Battlefield.shotAt(Coordinate(0,0))
        self.assertFalse(self.Battlefield.areAllSunk())
        ship = self.Battlefield.shotAt(Coordinate(0,0))
        self.assertFalse(self.Battlefield.areAllSunk())
        ship = self.Battlefield.shotAt(Coordinate(0,1))
        self.assertTrue(self.Battlefield.areAllSunk())

    def getFullCollection(self):
        collection = []
        collection.append(Ship(Carrier(),Coordinate(1,1),HorizontalDirection()))
        collection.append(Ship(Cruiser(),Coordinate(0,2),VerticalDirection()))
        collection.append(Ship(Destroyer(),Coordinate(4,2),VerticalDirection()))
        collection.append(Ship(Battleship(),Coordinate(7,5),VerticalDirection()))
        collection.append(Ship(Submarine(),Coordinate(2,9),VerticalDirection()))
        return collection

    def fillBattlefield(self):
        collection = self.getFullCollection()
        for ship in collection:
            self.Battlefield.addShip(ship)

    def getGenericShip(self,x,y,dir,name,length):
        Origin = Coordinate(x,y)
        Dir = Direction.Factory(dir)
        Type = ShipType(name,length)
        return Ship(Type,Origin,Dir)
