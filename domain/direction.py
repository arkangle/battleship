
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
    def inBetween(self,origin_x_y,length,try_x_y):
        pass
    def getRange(self,origin_x_y,length):
        pass

class HorizontalDirection(Direction):
    def getEndXY(self,x_y,length):
        return (x_y[0]+length,x_y[1])

    def inBetween(self,origin_x_y,length,try_x_y):
        if(origin_x_y[1] == try_x_y[1] and try_x_y[0] >= origin_x_y[0] and try_x_y[0] <= (origin_x_y[0]+length-1)):
            return True
        else:
            return False

    def getRange(self,x_y,length):
        r = []
        for x in range(x_y[0],x_y[0]+length):
            r.append((x,x_y[1]))
        return r

class VerticalDirection(Direction):
    def getEndXY(self,x_y,length):
        return (x_y[0],x_y[1]+length)

    def inBetween(self,origin_x_y,length,try_x_y):
        if(origin_x_y[0] == try_x_y[0] and try_x_y[1] >= origin_x_y[1] and try_x_y[1] <= (origin_x_y[1]+length-1)):
            return True
        else:
            return False

    def getRange(self,x_y,length):
        r = []
        for y in range(x_y[1],x_y[1]+length):
            r.append((x_y[0],y))
        return r

