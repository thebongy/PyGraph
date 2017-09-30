class Axis(object):
    def __init__(self,axis,scale=1,size):
        self.axis = axis
        self.scale = scale
        self.size = size

        if axis == 'x':
            self.position = Point(0, size.y-1)
        else:
            self.position = Point(0,0)
        
        self.count = 15.0
        self.least_count = 0
        self.markings = []
        self.display = []
    
    def calc_markings(self,_range):
        self.least_count = (_range.hi - _range.lo)/self.count


