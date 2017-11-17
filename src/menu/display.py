from inputhandler import InputHandler
def get_title():
	title = open("title.txt")
	title_data = []
	for line in title.readlines():
		title_data.append(list(line))
	return title_data


class Menu():
	def __init__(self, Terminal, EventManager):
		EventManager.add_listener(ArrowKey,self)
		EventManager.add_listener(EnterKey, self)
		self.currentOption = 0
		graphpos = 0
		graphlen = 5
		graphrect = Rect(graphpos,graphlen)
		
		helppos = 0
		helplen = 4
		helprect = Rect(helppos,helplen)
		
		aboutpos = 0
		aboutlen = 5
		aboutrect = Rect(aboutpos,aboutlen)
		
		exitpos = 0
		exitlen = 4
		exitrect = Rect(exitpos,exitlen)
		
		titlepos = 0
		titlerect = Rect(titlepos, 42)
		titledata = get_title()
		self.titleSurface = Surface(titlerect, titledata)
		
		self.options = [Text("Graph", graphrect), Text("Help", helprect), Text("Exit", exitrect)]
		self.T = Terminal
	
	def display(self):
		self.T.draw(self.titleSurface)
		for op in self.options:
			self.T.draw(op)
	
	def update(self, event):
		if isinstance(event, ArrowKey):
			if event.direction == RIGHT:
				if self.currentOption != 3:
					self.currentOption += 1
				else:
					self.currentOption = 0
	
			elif event.direction == LEFT:
				if self.currentOption != 0:
					self.currentOption -= 1
				else:
					self.currentOption = 3
		elif isinstance(event, EnterKey):
			pass
	
		
	
		
		
		
		