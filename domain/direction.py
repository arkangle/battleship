
class Direction:
    @staticmethod
    def Factory(name):
        n = name[0].lower()
        if(n == 'h'):
            return HorizontalDirection()
        elif(n == 'v'):
            return VerticalDirection()

    def getEndXY(self,x_y,length):
        pass

class HorizontalDirection(Direction):
    def getEndXY(self,x_y,length):
        return (x_y[0]+length,x_y[1])

class VerticalDirection(Direction):
    def getEndXY(self,x_y,length):
        return (x_y[0],x_y[1]+length)
