class Size(object):
    def __init__(self,width,height)
        self.width = width
        self.height = height
        
        self.x = width-1 # Last x_coordinate on the Size
        self.y = height-1 # Last y_cordinate on the Size

    def __repr__(self):
        self.dict_rep = {"width":width,"height":height}
        return self.dict_rep

def Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
