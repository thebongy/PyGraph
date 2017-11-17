from inputhandler import InputHandler
class OptionSelectedEvent():
	def __init__(self, name):
		self.name = name

def get_title():
	title = open("title.txt")
	title_data = []
	for line in title.readlines():
		title_data.append(list(line))
	return title_data


class Menu():
	def __init__(self,EventManager):
		self.ev = EventManager
		EventManager.add_listener(ArrowKey,self)
		EventManager.add_listener(EnterKey, self)
		EventManager.add_listener(Display, self)
		self.currentOption = 0
		self.option_selected = False
		
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
		
		self.options = [Text("Graph", graphrect), Text("Help", helprect), Text("About", aboutrect), Text("Exit", exitrect)]
	
	def display(self, terminal):
		terminal.draw(self.titleSurface)
		for op in self.options:
			terminal.draw(op)
	
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
			self.option_selected = True
		elif isinstance(event, Display):
			if self.option_selected:
				self.ev.update(OptionSelectedEvent(self.options[self.option_selected].text))

				
def Graph(terminal):
	print "Graph Selected"

def Help(terminal):
	
	
class OptionHandler(object):
	def __init__(self, EventManager):
		self.ev =  EventManager
		self.option_selected = False
		self.options = {
			"Graph": Graph,
			"Help": Help,
			"About": About,
			"Exit": Exit
		}
		EventManager.add_listener(OptionSelectedEvent, self)
		EventManager.add_listener(Display, self)
		EventManager.add_listener(EnterKey, self)
		
	def update(self, event):
		if isinstance(event, OptionSelectedEvent):
			self.option_selected = event.name
		elif isinstance(event, Display):
			self.options[self.option_selected](event.terminal)
				
	
		
	
		
		
		
		