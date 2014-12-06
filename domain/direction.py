class Direction:
    @staticmethod
    def Factory(name):
        n = name[0].lower()
        if(n == 'h'):
            return HorizontalDirection()
        elif(n == 'v'):
            return VerticalDirection()

    def nextXY(self,x_y):
        pass

class HorizontalDirection(Direction):
    def nextXY(self,x_y):
        return (x_y[0] + 1,x_y[1])

class VerticalDirection(Direction):
    def nextXY(self,x_y):
        return (x_y[0],x_y[1] + 1)
