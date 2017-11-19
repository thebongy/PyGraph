from msvcrt import getch
UP, DOWN, LEFT, RIGHT = range(4)

directions = {72:UP, 77:RIGHT, 75:LEFT, 80: DOWN}

class ArrowKey():
	def __init__(self, direction):
		self.direction = direction
class EnterKey():
	pass

class EscapeKey():
	pass

def InputHandler(EventManager):
	x = ord(getch())
	if (x == 224):
		x = ord(getch())
		direct = directions[x]
		EventManager.update(ArrowKey(direct))
	elif (x == 13):
		EventManager.update(EnterKey())
	elif (x==27):
		EventManager.update(EscapeKey())
		
InputHandler()