
class Ship:
  def __init__(self,name,length):
    self.name=name
    self.length=length

  def getLength(self):
    return self.length

  def getName(self):
    return self.name

class Battleship(Ship):
  def __init__(self):
    Ship.__init__(self,"Battleship",4)

class Carrier(Ship):
  def __init__(self):
    Ship.__init__(self,"Carrier",5)

class Cruiser(Ship):
  def __init__(self):
    Ship.__init__(self,"Cruiser",3)

class Destroyer(Ship):
  def __init__(self):
    Ship.__init__(self,"Destroyer",2)

class Submarine(Ship):
  def __init__(self):
    Ship.__init__(self,"Submarine",3)

