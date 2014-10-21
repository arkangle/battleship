
class Direction:
    @staticmethod
    def Factory(name):
        n = name[0].lower()
        if(n == 'h'):
            return HorizontalDirection()
        elif(n == 'v'):
            return VerticalDirection()

    def getEndXY(self,x_y,length):
        list_x_y = list(x_y)
        list_x_y[self.i_change] += length
        return tuple(list_x_y)

    def inBetween(self,origin_x_y,length,try_x_y):
        if(origin_x_y[self.i_same] == try_x_y[self.i_same] and
                try_x_y[self.i_change] >= origin_x_y[self.i_change] and
                try_x_y[self.i_change] <= (origin_x_y[self.i_change]+length-1)):
            return True
        else:
            return False

    def getRange(self,x_y,length):
        r = []
        for change in range(x_y[self.i_change],x_y[self.i_change]+length):
            list_x_y = [0,0]
            list_x_y[self.i_change] = change
            list_x_y[self.i_same] = x_y[self.i_same]
            r.append(tuple(list_x_y))
        return r


class HorizontalDirection(Direction):
    def __init__(self):
        self.i_change = 0
        self.i_same = 1

class VerticalDirection(Direction):
    def __init__(self):
        self.i_change = 1
        self.i_same = 0

