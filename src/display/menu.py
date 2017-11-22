from inputhandler import *
from render.utils import *
from postfix.parser import Expression

class OptionSelectedEvent():
	def __init__(self, no):
		self.no = no

class OptionHighlightedEvent():
	def __init__(self,no):
		self.no = no

class DisplayMainMenu():
	pass

def get_title():
	title = open("display/logo.txt","r")
	title_data = []
	for line in title.readlines():
		title_data.append(list(line))
	return title_data


class MainMenu(object):
	def __init__(self,EventManager, terminal):
		self.ev = EventManager
		self.terminal = terminal
		EventManager.add_listener(ArrowKey,self)
		EventManager.add_listener(EnterKey, self)
		EventManager.add_listener(Display, self)
		EventManager.add_listener(DisplayMainMenu, self)
		self.currentOption = 0
		self.showing = True
		self.titleSurface = Surface(Point(30,20),get_title())
		
		self.version = "1.0 Development Version"
		self.versionSurface = Text(Point(60,30), self.version)
		self.options = [
		Text(Point(30,35),"Graph"), 
		Text(Point(50,35), "Help"), 
		Text(Point(70,35), "About"), 
		Text(Point(90,35), "Exit")
		]
		
		self.optionHandler = OptionHandler(EventManager, self.options, terminal)
	
	def display(self):
		self.terminal.clear_data()
		self.showing = True
		self.terminal.draw(self.titleSurface)
		self.terminal.draw(self.versionSurface)
		for op in self.options:
			self.terminal.draw(op)
		self.terminal.update_screen()
	
	def update(self, event):
		if isinstance(event, DisplayMainMenu):
			self.display()
		if self.showing:
			if isinstance(event, ArrowKey):
				if event.direction == RIGHT:
					if self.currentOption != 3:
						self.currentOption += 1
					else:
						self.currentOption = 0
					self.ev.update(OptionHighlightedEvent(self.currentOption))
				elif event.direction == LEFT:
					if self.currentOption != 0:
						self.currentOption -= 1
					else:
						self.currentOption = 3
					self.ev.update(OptionHighlightedEvent(self.currentOption))
			elif isinstance(event, EnterKey):
				self.showing = False
				self.ev.update(OptionSelectedEvent(self.currentOption))

class MainContent(object):
	def __init__(self, title, ev, terminal):
		self.ev = ev
		self.title = title
		self.terminal = terminal
		self.showing = False
		self.titleSurface = Text(Point(0,1),title.center(100))
		self.mainBorder = Rectangle(Point(2,5), Size(115,44))
		self.contentSize = Size(112, 37)
		self.content = Surface(Point(3,6), [[]])
		self.misc = [] # All other required elements
	def display(self):
		self.beforeDisplayHooks()
		self.terminal.clear_data()
		self.showing = True
		self.terminal.draw(self.titleSurface)
		self.terminal.draw(self.mainBorder)
		self.terminal.draw(self.content)
		for obj in self.misc:
			self.terminal.draw(obj)
		self.terminal.update_screen()
		self.afterDisplayHooks()
	def update(self, event):
		raise NotImplementedError
	
	def beforeDisplayHooks(self):
		pass
	
	def afterDisplayHooks(self):
		pass

class EquationInput(MainContent):
	def __init__(self, ev, terminal):
		MainContent.__init__(self, "Graph", ev, terminal)
		self.block_enter_key = True
		self.input_box = InputBox(Point(8,25), 90)
		self.inputPrompt = Paragraph(Point(6, 20), Size(100,4),
		"""Please type in the math equation/function in the box below:
(Press Enter when you are Done)""")
		self.misc.append(self.input_box)
		self.misc.append(self.inputPrompt)
		ev.add_listener(EnterKey, self)
		ev.add_listener(EscapeKey, self)
		ev.add_listener(KeyPress, self)
		ev.add_listener(BackSpace, self)
		
	def update(self, event):
		if self.showing:
			if isinstance(event, EscapeKey):
				self.showing = False
				self.block_enter_key = True
				self.input_box.clearInput()
				self.clear_errors()
				self.ev.update(DisplayMainMenu())
			elif isinstance(event, KeyPress):
				self.input_box.input(chr(event.code))
				self.clear_errors()
				self.display()
			elif isinstance(event, BackSpace):
				self.input_box.backSpace()
				self.clear_errors()
				self.display()
			elif isinstance(event, EnterKey):
				if self.block_enter_key:
					self.block_enter_key = False
					return
				try:
					if self.input_box.text != "":
						expr = Expression(self.input_box.text)
						self.showing = False
						self.clear_errors()
						self.Graph_display = Graph(self.ev, self.terminal, expr, self)
						self.terminal.clear_screen()
						self.Graph_display.display()
					else:
						raise ValueError("Equation cannot be blank!!!")
				except Exception as e:
					if isinstance(self.misc[-1], Text):
						self.misc.pop()
					
					self.misc.append(Text(Point(8, 30), "Error!!!  " + e.message))
					self.display()
	
	def beforeDisplayHooks(self):
		self.Graph_display = None
	
	def clear_errors(self):
		if isinstance(self.misc[-1], Text):
			self.misc.pop()

class Graph(MainContent):
	def __init__(self, ev, terminal, expr, eqInput):
		MainContent.__init__(self, "Graph of " + expr.raw_expr, ev, terminal)
		
		self.eqInput = eqInput
		self.expr = expr
		ev.add_listener(EscapeKey, self)
		ev.add_listener(ArrowKey, self)
		ev.add_listener(KeyPress, self)
		self.content = Surface(Point(3,8), [[" " for i in range(self.contentSize.width)] for j in range(self.contentSize.height)])
		self.SCALEx = 0.1
		self.SCALEy = 0.1
		self.xCONSTANT = 0
		self.yCONSTANT = 0
		self.W = self.contentSize.width
		self.H = self.contentSize.height
		self.plot_function()
	
	def update(self, event):
		if self.showing:
			if isinstance(event, EscapeKey):
				self.showing = False
				self.eqInput.display()
			elif isinstance(event, ArrowKey):
				if (event.direction == RIGHT):
					self.xCONSTANT += 0.5
				elif (event.direction == LEFT):
					self.xCONSTANT -= 0.5
				elif (event.direction == UP):
					self.yCONSTANT += 0.5
				elif (event.direction == DOWN):
					self.yCONSTANT -= 0.5
				self.clear_graph()
				self.plot_function()
				self.display()
			elif isinstance(event, KeyPress):
				valid = True
				char = chr(event.code)
				if char == "X":
					self.SCALEx -= 0.01
				elif char == "x":
					self.SCALEx += 0.01
				elif char == "y":
					self.SCALEy += 0.01
				elif char == "Y":
					self.SCALEy -= 0.01
				elif char == "r":
					self.SCALEx = 0.1
					self.SCALEy = 0.1
					self.xCONSTANT = 0
					self.yCONSTANT = 0
				elif char == "z":
					self.SCALEx += 0.01
					self.SCALEy += 0.01
				elif char == "Z":
					self.SCALEx -= 0.01
					self.SCALEy -= 0.01
				else:
					valid = False
				
				if valid:
					self.clear_graph()
					self.plot_function()
					self.display()
	
	def clear_graph(self):
		for i in range(self.contentSize.height):
			for j in range(self.contentSize.width):
				self.content.data[i][j] = " "
				
	def plot_function(self):
		X = [(self.xCONSTANT + (self.SCALEx * i)) for i in range(0,self.W)]
		Y = [(self.yCONSTANT - 2 + (self.SCALEy * i)) for i in range(0,self.H)]

		GOP = []
		Clist = ['T','T']
		prevY = None
		for i in range(len(X)):
			try:
				GOP.append(self.expr.evaluate((X[i])))
			except ZeroDivisionError:
				GOP.append(10000000000000000000.0)
			except Exception as e:
				print e.message
			if i > 1:
				if GOP[-1] > Y[-1] or GOP[-1] < Y[0]:
					Clist.append('D')
				elif GOP[-1] > GOP[-2]:
					Clist.append('>')
				elif GOP[-1] < GOP[-2]:
					Clist.append('<')
				else:
					Clist.append('=')

			t = True
			for j in range(len(Y)):
				if Y[j] == GOP[-1] and t:
					self.content.data[self.H-j-1][i] = "*"
					t = False
				elif GOP[-1] < Y[j] and t and GOP[-1] >= Y[0]:
					if j != 0:
						self.content.data[self.H-j][i] = "*"
					self.content.data[self.H-j-1][i] = "*"
					t = False
				
				if (len(GOP) > 1) and (not t) and (j > 1):
					if (GOP[-1]-GOP[-2]) > self.SCALEy:
						for g in range(prevY, (prevY+j)/2):
							self.content.data[self.H-1-g][i-1] = "*"
						for g in range((prevY+j)/2, j):
							self.content.data[self.H-1-g][i] = "*"
					elif (GOP[-2]-GOP[-1]) > self.SCALEy:
						for g in range((prevY+j)/2-1,prevY):
							self.content.data[self.H-1-g][i-1] = "*"
						for g in range(j, (prevY+j)/2):
							self.content.data[self.H-1-g][i] = "*"
					break
			prevY = j
		
		
		
		
class Help(MainContent):
	def __init__(self, ev, t):
		MainContent.__init__(self, "Help", ev, t)
		self.content = Paragraph(Point(4,7), Size(90, 30), open("display/help.txt").read())
		ev.add_listener(EscapeKey, self)
	
	def update(self, event):
		if self.showing:
			if isinstance(event, EscapeKey):
				self.showing = False
				self.ev.update(DisplayMainMenu())

class About(MainContent):
	def __init__(self, ev, t):
		MainContent.__init__(self, "About", ev, t)
		self.content = Paragraph(Point(4,7), Size(90, 30), open("display/about.txt").read())
		ev.add_listener(EscapeKey, self)
	def update(self, event):
		if self.showing:
			if isinstance(event, EscapeKey):
				self.showing = False
				self.ev.update(DisplayMainMenu())


class OptionHandler(object):
	def __init__(self, EventManager, optionSurfaces, terminal):
		self.ev =  EventManager
		self.option_selected = False
		self.terminal = terminal
		self.option_highlighted = 0
		self.optionFuncs = [
			EquationInput(self.ev, terminal),
			Help(self.ev, terminal),
			About(self.ev, terminal)
		]
		self.options = optionSurfaces
		
		EventManager.add_listener(OptionSelectedEvent, self)
		EventManager.add_listener(OptionHighlightedEvent, self)
		
		self.highlightOption()
	def highlightOption(self):
		for i,option in enumerate(self.options):
			if i == self.option_highlighted:
				option.highlight()
			else:
				option.unhighlight()
		self.ev.update(DisplayMainMenu())
	def update(self, event):
		if isinstance(event, OptionSelectedEvent):
			if event.no == 3:
				self.terminal.clear_screen()
				print "Thank You for using PyGraph :)"
				exit()
			self.option_selected = event.no
			self.optionFuncs[event.no].display()
		elif isinstance(event, OptionHighlightedEvent):
			self.option_highlighted = event.no
			self.highlightOption()
				
	
		
	
		
		
		
		