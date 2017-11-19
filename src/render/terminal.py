import platform
from os import system
from utils import *

class Terminal(Surface):
	def __init__(self,size):
		Surface.__init__(self, Point(0,0), [[" " for i in range(size.width)] for j in range(size.height)])
		self.os = platform.system() # Get the User's Operating System

		if self.os == "Windows":
			self.clear_command = "cls"
			self.resize_command = "mode %s,%s" % (size.width+1, size.height+1)
		else:
			self.clear_command = "clear"
			self.resize_command = "printf '\e[8;%s;%st'" % (size.height+1, size.width+1)
		
		self.resize_screen(size)
	
	def update_screen(self):
		self.clear_screen()
		for row in self.data:
			print "".join(row)
	
	def clear_data(self):
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				self.data[i][j] = " "
	def clear_screen(self):
		# Clear Terminal/CMD screen
		system(self.clear_command)

	def resize_screen(self,size):
		system(self.resize_command)

