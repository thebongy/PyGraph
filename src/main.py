from render.EventManager import EventManager
from render.utils import *
from render.terminal import Terminal
from display.menu import Menu
from display.inputhandler import *

size = Size(120,50)


terminal = Terminal(size)
ev = EventManager()
menu = Menu(ev)
menu.display(terminal)

