class Rect(object):
    def __init__(self,pos, size):
        self.tl = pos
        self.tr = Point(pos.x+size.width, pos.y)
        self.bl = Point(pos.x, pos.y + size.height)
        self.br = Point(pos.x + size.width, pos.y+ size.height)

        self.left = pos.x
        self.right = pos.x + self.width
        self.top = pos.y
        self.bottom = pos.y+ self.height

        self.center = Point((pos.x+size.width)/2, (pos.y+size.height)/2)
    
    def inRect(self,Point):
        if (self.left <= Point.x <= self.right) and (self.top <= Point.y <= self.bottom):
            return True
        return False

class Size(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Text(Surface):
	def __init__(self, text, rect):
		Surface.__init__(self, rect, list(text))


class Surface(object):
    def __init__(self, rect, data):
        self.rect = rect
        self.data = data
    
    def draw(self, surface):
        for x in range(surface.rect.left, surface.rect.right):
            for y in range(surface.rect.top, surface.rect.bottom):
                self.data[y][x] = surface.data[y-surface.rect.top][x-surface.rect.left]
